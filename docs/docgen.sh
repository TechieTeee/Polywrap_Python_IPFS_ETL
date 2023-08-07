sphinx-apidoc ../packages/polywrap-msgpack/polywrap_msgpack -o ./source/polywrap-msgpack -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/polywrap-manifest/polywrap_manifest -o ./source/polywrap-manifest -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/polywrap-core/polywrap_core -o ./source/polywrap-core -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/polywrap-wasm/polywrap_wasm -o ./source/polywrap-wasm -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/polywrap-plugin/polywrap_plugin -o ./source/polywrap-plugin -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/polywrap-uri-resolvers/polywrap_uri_resolvers -o ./source/polywrap-uri-resolvers -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/polywrap-client/polywrap_client -o ./source/polywrap-client -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/polywrap-client-config-builder/polywrap_client_config_builder -o ./source/polywrap-client-config-builder -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/plugins/polywrap-fs-plugin/polywrap_fs_plugin -o ./source/polywrap-fs-plugin -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/plugins/polywrap-http-plugin/polywrap_http_plugin -o ./source/polywrap-http-plugin -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/plugins/polywrap-ethereum-provider/polywrap_ethereum_provider -o ./source/polywrap-ethereum-provider -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/config-bundles/polywrap-sys-config-bundle/polywrap_sys_config_bundle -o ./source/polywrap-sys-config-bundle -e  -M -t ./source/_templates -d 2
sphinx-apidoc ../packages/config-bundles/polywrap-web3-config-bundle/polywrap_web3_config_bundle -o ./source/polywrap-web3-config-bundle -e  -M -t ./source/_templates -d 2

cd ../packages/polywrap-client && python scripts/extract_readme.py && cd ../../docs
cp ../packages/polywrap-client/README.rst ./source/Quickstart.rst