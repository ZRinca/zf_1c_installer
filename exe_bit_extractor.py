import struct

IMAGE_FILE_MACHINE_I386 = 332
IMAGE_FILE_MACHINE_IA64 = 512
IMAGE_FILE_MACHINE_AMD64 = 34404
IMAGE_FILE_MACHINE_ARM = 452
IMAGE_FILE_MACHINE_AARCH64 = 43620


def exe_bit(path_to_the_exe):
    try:
        with open(path_to_the_exe, 'rb') as f:
            s = f.read(2)
            if s != b'MZ':
                return 'Not an EXE file'
            else:
                f.seek(60)
                s = f.read(4)
                header_offset = struct.unpack('<L', s)[0]
                f.seek(header_offset + 4)
                s = f.read(2)
                machine = struct.unpack('<H', s)[0]

                if machine == IMAGE_FILE_MACHINE_I386:
                    return 32
                elif machine == IMAGE_FILE_MACHINE_IA64:
                    return 64
                elif machine == IMAGE_FILE_MACHINE_AMD64:
                    return 64
                elif machine == IMAGE_FILE_MACHINE_ARM:
                    return 32
                elif machine == IMAGE_FILE_MACHINE_AARCH64:
                    return 64
                else:
                    #return f'Unknown architecture {machine}'
                    return f'Unknown architecture'
    except FileNotFoundError:
        return "Мы не смогли найти 1с"
