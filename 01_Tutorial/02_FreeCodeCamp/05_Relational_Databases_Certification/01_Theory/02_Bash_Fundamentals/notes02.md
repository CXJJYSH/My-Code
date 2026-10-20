# Understanding the Command Line and Working with Bash

## 1. What is the terminal, and how does it differ from the command line?

The command line is a basic text input interface which allows a user to enter "commands", usually in the form of a series of characters, and submit or execute them, usually by pressing the Enter key. You will most commonly see command line interfaces within a terminal.

A terminal is a special application that offers a command line interface to perform system-level commands beyond the basic read/write operations. You may also hear about "terminal emulators", which are essentially applications that wrap a basic terminal interface to offer additional features or functionality. But for most general purposes, you are probably safe to refer to these as "terminals" as well.

Finally, we will also need to talk about "shells". A shell is the software that wraps the command line and interprets your inputs as commands, returning the output.

## 2. What Are Some Shortcuts You Can Use in the Command Line to Speed Up Productivity?

## 3. What Is Bash, and What Are Some Basic Commands?

Bash = Bourne Again SHell

pwd = print working directory

cd = change directory

ls = list

less

cat

mv = move (or rename)

rm = remove (or delete)

cp = copy

## 4. What Are Some Command Options and Flags?

## 5. How Do You Configure Your System Language for Bash and PostgreSQL Workshops?

# Workshop

## 1. Build a Boilerplate

```
1. Restart Terminal
2. Print Working Directory
3. List
4. Change Directory
5. Print Working Directory
6. List
7. Change Directory
8. Print Working Directory
9. List
10. Change Directory
11. List
12. More
13. Clear
14. List
15. Change Directory
16. List
17. Long List Format
18. Change Directory
19. List
20. More
21. List
22. More
23. Clear
24. List
25. Change Directory
26. Print Working Directory
27. List
28. More
29. Change Directory
30. Change Directory
31. Change Directory
32. List
33. Clear
34. Make Directory
35. List
36. Change Directory
37. List
38. Echo
39. Touch
40. Touch
41. List
42. Touch
43. Touch
44. List
45. Help
46. List All
47. Change Directory
48. Touch
49. Touch
50. Touch
51. List
52. Touch
53. Touch
54. Touch
55. List
56. Touch
57. Touch
58. Touch
59. List
60. Make Directory
61. List
62. Copy
63. Change Directory
64. List
65. Change Directory
66. List
67. Remove
68. List
69. Copy
70. Copy
71. Change Directory
72. List
73. Change Directory
74. List
75. Remove
76. Remove
77. List
78. Rename
79. List
80. Rename
81. Rename
82. List
83. Make Directory
84. List
85. Move
86. Find
87. Move
88. Move
89. Find
90. Make Directory
91. Make Directory
92. Move
93. Find
94. Move
95. Move
96. Find
97. Find Subfolder
98. Find
99. Find
100. Find
101. Find
102. Find
103. Change Directory
104. Make Directory
105. Change Directory
106. Make Directory
107. Change Directory
108. Touch
109. Change Directory
110. Change Directory
111. List
112. Move
113. List
114. Change Directory
115. List
116. Find
117. Move
118. Find
119. Find
120. Move
121. Find
122. Remove Directory
123. Remove
124. Remove Directory
125. List
126. Make Directory
127. Move
128. Find
129. Move
130. Move
131. Find
132. Make Directory
133. Touch
134. Touch
135. Find
136. Touch
137. Touch
138. Find
139. Remove Help
140. Remove Recursively
141. List
142. Touch
143. Touch
144. Touch
145. List
146. Echo
147. Echo
148. Echo
149. Echo to File
150. More
151. Echo to File
152. More
153. Echo to File
154. More
155. Change Directory
156. List
157. Rename
158. List
159. Copy Help
160. Copy
161. List
162. Find
163. Find
164. Clear
165. Echo
166. Exit
```

# Bash Commands Review

## Terminal, Shell, and Command Line Basics

- Command line: A text interface where users type commands.
- Terminal: The application that provides access to the command line.
- Terminal emulator: Adds extra features to a terminal.
- Shell: Interprets the commands entered into the terminal (e.g., Bash).
- PowerShell / Command Prompt / Microsoft Terminal: Options for accessing the command line on Windows.
- Terminal (macOS): Built-in option on macOS, with third-party alternatives like iTerm or Ghostty.
- Terminal (Linux): Options vary by distribution, with many third-party emulators like kitty.
- Terminology: Though "terminal," "shell," and "command line" are often used interchangeably, they have specific meanings.

## Command Line Shortcuts

- Up Arrow/Down Arrow: Cycle through previous/next commands in history.
- Tab: Autocomplete commands.
- Control + L (Linux/macOS) or typing `cls` (Windows): Clear the terminal screen.
- Control + C: Interrupt a running command (also used for copying in PowerShell if text is selected).
- Control + Z (Linux/macOS only): Suspend a task to the background; use `fg` to resume it.
- `!!`: Instantly rerun the last executed command.

## Bash Basics

Bash (Bourne Again Shell): Widely used Unix-like shell.

Key commands:

- `pwd`: Show the current directory.
- `cd`: Change directories.
- `..` refers to the parent directory (one level up).
- `.` refers to the current directory.
- `ls`: List files and folders.
  - `-a`: Show all files, including hidden files.
  - `-l`: Show detailed information about files.
- `less`: View file contents one page at a time with navigation options, including scrolling backward and searching.
- `more`: Display file contents one screen at a time, with limited backward scrolling and basic navigation.
- `cat`: Show the entire file content at once without scrolling or navigation, useful for smaller files.
- `mkdir`: Create a new directory.
- `rmdir`: Remove an empty directory.
- `touch`: Create a new file.
- `mv`: Move or rename files.
  - Rename: `mv oldname.txt newname.txt`
  - Move: `mv filename.txt /path/to/target/`
- `cp`: Copy files.
  - `-r`: Recursively copy directories and their contents.
- `rm`: Delete files.
  - `-r`: Recursively delete directories and their contents.
- `echo`: Display a line of text or a variable's value.
  - Use `>` to overwrite the existing content in a file (e.g., `echo "text" > file.txt`).
  - Use `>>` to append output to a file without overwriting existing content (e.g., `echo "text" >> file.txt`).
- `exit`: Exit the terminal session.
- `clear`: Clear the terminal screen.
- `find`: Search for files and directories.
  - `-name`: Search for files by name pattern (e.g., `find . -name "*.txt"`).
- Use `man` followed by a command (e.g., `man ls`) to access detailed manual/help pages.

## Command Options and Flags

Options or flags: Modify a command's behavior and are usually prefixed with hyphens.

- Long form (two hyphens):
  - Examples: `--help`, `--version`
  - Values are attached using an equals sign, e.g., `--width=50`.
- Short form (one hyphen):
  - Examples: `-a`, `-l`
  - Values are passed with a space, e.g., `-w 50`.
  - Multiple short options can be chained together, e.g., `ls -alh`.
- `--help`: You can use this flag with many commands to understand the available options.

# Bash Commands Quiz

To pass the quiz, you must correctly answer at least 18 of the 20 questions below.

cat = concatenate

100%.

2026.10.19 21:21
