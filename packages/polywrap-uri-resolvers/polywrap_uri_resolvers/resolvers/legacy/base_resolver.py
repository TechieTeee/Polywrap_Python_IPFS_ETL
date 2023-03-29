from typing import Dict

from polywrap_core import (
    InvokerClient,
    IFileReader,
    IUriResolutionContext,
    UriResolver,
    Uri,
    UriPackageOrWrapper,
)

from .fs_resolver import FsUriResolver
from .redirect_resolver import RedirectUriResolver


class BaseUriResolver(UriResolver):
    _fs_resolver: FsUriResolver
    _redirect_resolver: RedirectUriResolver

    def __init__(self, file_reader: IFileReader, redirects: Dict[Uri, Uri]):
        self._fs_resolver = FsUriResolver(file_reader)
        self._redirect_resolver = RedirectUriResolver(redirects)

    async def try_resolve_uri(
        self, uri: Uri, client: InvokerClient[UriPackageOrWrapper], resolution_context: IUriResolutionContext[UriPackageOrWrapper]
    ) -> UriPackageOrWrapper:
        redirected_uri = await self._redirect_resolver.try_resolve_uri(
            uri, client, resolution_context
        )

        return await self._fs_resolver.try_resolve_uri(
            redirected_uri, client, resolution_context
        )
