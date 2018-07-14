This is a simple template of just creating your NEO token.

- yourcoin directory is a main your token base
- yourcoin-smartcontract.py is base file of smart contract

# Usage

Firstly, you should make neo-python environment.
https://github.com/CityOfZion/python-smart-contract-workshop#quickstart

Then, create your token in your private network.

以下のコマンドは当リポジトリのディレクトリ上で行うか、適宜pathを変えてください。
また [こちら](https://s3.amazonaws.com/neo-experiments/neo-privnet.wallet)からneo-privnet.walletを当リポジトリのwalletsディレクトリにダウンロードしてください。

0. open wallet {neo-privnet.wallet path}
0. neo-privnet.walletをopenを開きます。passwordは「coz」です
1. Change TOKEN_ORNER value to your wallet script hash in yourcoin/token.py
1. PULLしたディレクトリのyourcoin/token.pyの定数、TOKEN_ORNERをnp-prompt -v -pでneo-pythonにアクセスし、neo-privnet.walletのscript hashを確認し、書き換えてください。

以下コマンドを、当リポジトリのディレクトリ上で実行してください。

2. build ./yourcoin-smartcontract.py test 0710 05 True False name []
3. import contract yourcoin-smartcontract.avm 0710 05 True False // Lastly you need to input wallet password and wait a few minutes)
4. testinvoke {contract hash} deploy [] // You need wallet password
5. import token {contract hash}
Now, you created your token and you have all your tokens.Check your wallet address.

Next, try send token another wallet.

For example

```

send yourcoin AX8r7K295FBQynTmbJw5PjsiY88JeTfpGh 100 --from-addr=AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y

```


References

- https://github.com/neonexchange/neo-ico-template
- http://neo-python.readthedocs.io/en/latest/index.html
- https://medium.com/proof-of-working/how-to-build-an-ico-on-neo-with-the-nex-ico-smart-contract-template-1beac1ff0afd


# Note

- "name []" in build command is mycoin-smartcontract.py's arguments.
- Many codes in [NEO ICO template]'s ico_template.py are necessary to comply NEP5.Because once you build your smart-contract, necessary commands depent on your smart-contract program.
- If you want to create new private network, stop and start(not restart) docker container and rm -rf ~/.neopython
