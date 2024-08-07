from logic.agent_mode import enter_commands_agent_mod
from logic.command_line_and_permissions import sub_run


def install_extension(caller_window, global_config):
    one_c_user = global_config['One_C_the_user']
    one_c = global_config['One_C']

    if "1cv8t" in one_c[one_c_user]:
        designer_command = [
            r"C:\Program Files\1cv8\common\1cestartt.exe",
            "DESIGNER",
            "/AgentMode",
            "/AgentBaseDir", r"C:\Apache24\Api",
            "/IBName", global_config['base_the_One_C'],
            "/AgentSSHHostKeyAuto",
            "/Visible"
        ]

        print(sub_run(designer_command))
    else:
        designer_command = [
            r"C:\Program Files\1cv8\common\1cestart.exe",
            "DESIGNER",
            "/AgentMode",
            "/AgentBaseDir", r"C:\Apache24\Api",
            "/IBName", global_config['base_the_One_C'],
            "/AgentSSHHostKeyAuto",
            "/Visible"
        ]

        print(sub_run(designer_command))
    enter_commands_agent_mod(global_config['LOGIN'], global_config['PASSWORD'])

    caller_window.open_next_window()