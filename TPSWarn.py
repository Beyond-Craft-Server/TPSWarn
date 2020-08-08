def form_msg(msg):
    message = '§a[§6Server thread§f/§cWARN§a]§f{}'.format(msg)
    return message


def on_info(server, info):
    if info.is_player is not True and info.content.startswith("Can't keep up! Is the server overloaded? Running"):
        msg = info.content
        server.say(form_msg(msg))
    else:
        pass