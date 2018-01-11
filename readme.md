## What is that?
> Main idea behind this small project is to automatize tests at C/C++ programs with Python. You can make predefined sets, which will be used to performe tests. Also, at enter you can choose output saving option: to file or send to you mail. Both names you should write at info.txt file (default)

##### Run example:
`python setPy -p program -t file -s sets.txt -o info.txt -i set1`

##### Let me explain parameters behind that:
> -p/--program {param}, where at {param} is program name

> -t/--output-type {param}, where {param} has value 'mail' or 'file' - give information to script about type of output

> -s/--input-sets {param}, where at {param} is file with data sets (check file: sets.txt)

> -o/--output {param}, where at {param} is name of file with information about output email adress or output file name

> -i/--input-file {param}, where at {param} is input data file for program

## To-Do
- [x] Finish first part of program - give main functionality
- [ ] Add daemon/threading
- [ ] Mail sending tests
- [ ] Extend parameters options