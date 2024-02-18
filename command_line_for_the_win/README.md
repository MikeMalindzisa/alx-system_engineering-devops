command_line_for_the_win

##SFTP Upload

#Local Machine
- Created cmd dir
- Saved .jpg and .png  files in the cmd dir

#Terminal Steps

- Connected to my remote sandbox using "sftp username@sandbox.host_name"
- Provided sandbox password on prompt
- Navigated to the local dir created before usind "lcd C:/User/LocalMachine/Pictures/cmd/"
- Navigated to my remote dir using "cd root/alx-system_engineering-devops/command_line_for_the_win/"
- Uploaded .jpg files using "put *_9_tasks*.jpg"
- Uploaded .png files using "put *_9_tasks*.png"
- Terminated the SFTP session using "exit"
