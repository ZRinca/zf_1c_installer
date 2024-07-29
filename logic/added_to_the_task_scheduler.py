from logic.command_line_and_permissions import sub_run


def added_task():
    command = ['SCHTASKS', '/Create', '/TN', 'zf_connector', '/XML', r'C:\Apache24\Api\ZFConnector_settings.xml']
    sub_run(command)
