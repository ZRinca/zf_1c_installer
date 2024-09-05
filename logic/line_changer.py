import re


def insert_new_line_in_file(input_file, output_file, insert_after_pattern, new_line):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = re.compile(f'({insert_after_pattern})', re.DOTALL)
        content_new = pattern.sub(rf'\1\n{new_line}', content)

        with open(output_file, 'w', encoding='utf-8') as fout:
            fout.write(content_new)

        print(f'Строка успешно добавлена и записана в файл: {output_file}')
    except IOError as e:
        print(f'Ошибка при чтении или записи файла: {e}')


def insert_a_line(line):

    insert_after_pattern = r'ib="File=&quot;C:\\bases\\buh&quot;;">'
    new_line = '''    <ws publishExtensionsByDefault="true">
        <point name="AccHRMDataTransfer"
                alias="AccHRMDataTransfer.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="EnterpriseDataExchange_1_0_1_1"
                alias="EnterpriseDataExchange_1_0_1_1.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="EnterpriseDataUpload_1_0_1_1"
                alias="EnterpriseDataUpload_1_0_1_1.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="EquipmentService"
                alias="EquipmentService.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="Exchange"
                alias="exchange.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="Exchange_2_0_1_6"
                alias="exchange_2_0_1_6.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="Exchange_3_0_1_1"
                alias="exchange_3_0_1_1.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="Exchange_3_0_2_1"
                alias="exchange_3_0_2_1.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="Exchange_3_0_2_2"
                alias="exchange_3_0_2_2.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="InterfaceVersion"
                alias="InterfaceVersion.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="MobileAccounting"
                alias="MobileAccounting.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="MobileEntrepreneur"
                alias="MobileAcc.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="MobileEntrepreneur_1_0_2_1"
                alias="MobileEntrepreneur.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="RemoteAdministrationOfExchange"
                alias="RemoteAdministrationOfExchange.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="RemoteAdministrationOfExchange_2_0_1_6"
                alias="RemoteAdministrationOfExchange_2_0_1_6.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="RemoteAdministrationOfExchange_2_1_6_1"
                alias="RemoteAdministrationOfExchange_2_1_6_1.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="RemoteAdministrationOfExchange_2_4_5_1"
                alias="RemoteAdministrationOfExchange_2_4_5_1.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <point name="RemoteControl"
                alias="RemoteControl.1cws"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
    </ws>
    <httpServices publishExtensionsByDefault="true">
        <service name="ExternalAPI"
                rootUrl="api"
                enable="true"
                reuseSessions="dontuse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <service name="MobileAppReceiptScanner"
                rootUrl="MobileAppReceiptScanner"
                enable="true"
                reuseSessions="autouse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <service name="payment"
                rootUrl="payment"
                enable="true"
                reuseSessions="autouse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <service name="Биллинг"
                rootUrl="billing"
                enable="true"
                reuseSessions="autouse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <service name="ПередачаДанных"
                rootUrl="dt"
                enable="true"
                reuseSessions="use"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
        <service name="ЭДО"
                rootUrl="edi"
                enable="true"
                reuseSessions="autouse"
                sessionMaxAge="20"
                poolSize="10"
                poolTimeout="5"/>
    </httpServices>
    <standardOdata enable="true"
            reuseSessions="autouse"
            sessionMaxAge="20"
            poolSize="10"
            poolTimeout="5"/>
    <analytics enable="true"/>'''

    insert_new_line_in_file(line, line, insert_after_pattern, new_line)


def extract_version_from_rc(file_path='version_info.rc', version_type='filevers'):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

    pattern = rf'{version_type}=\((\d+), (\d+), (\d+), (\d+)\)'
    version_match = re.search(pattern, content)
    return ".".join(version_match.groups())
