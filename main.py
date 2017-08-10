import itchatmp
from itchatmp.content import TEXT

itchatmp.update_config(itchatmp.WechatConfig(
    token='123',
    appId = 'wx4ee76049687c28b4',
    appSecret = 'fd31941e5cec53ae1bf2a2ce97c3a9bb'))

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    print(msg)
    return 'I received: ' + msg['Text']

itchatmp.run()
