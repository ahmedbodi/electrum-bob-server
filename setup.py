from setuptools import setup

setup(
    name="electrum-bob-server",
    version="1.0",
    scripts=['run_electrum_bob_server.py','electrum-bob-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumbobserver':'src'
        },
    py_modules=[
        'electrumbobserver.__init__',
        'electrumbobserver.utils',
        'electrumbobserver.storage',
        'electrumbobserver.deserialize',
        'electrumbobserver.networks',
        'electrumbobserver.blockchain_processor',
        'electrumbobserver.server_processor',
        'electrumbobserver.processor',
        'electrumbobserver.version',
        'electrumbobserver.ircthread',
        'electrumbobserver.stratum_tcp',
        'electrumbobserver.stratum_http'
    ],
    description="Dobbscoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/pooler/electrum-bob-server/",
    long_description="""Server for the Electrum Lightweight Dobbscoin Wallet"""
)
