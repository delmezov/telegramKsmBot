def save_log_to_file(file_path, str_log):
    open_file = open(file_path, 'a')
    open_file.write(str_log + "\n")