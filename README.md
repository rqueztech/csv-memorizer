# CSV Memorizer Tool

## Purpose
- The CSV Memorizer tool is a simple tool that reads a csv (must include headers), and allows you to rotate your data out for rote memorization.
- It is very common that you just want to see your data represented with different key value pairs to see if you can detect patterns. This program will interactively allow you to rotate out your information.
- Unglamorous but effective at taking your lists, grouping them in different ways so you can check pattern. Essentially you can take any column, turn that to the key, and the program does the grouping for you.

## Why Not Pandas?
Pandas is the absolute GOAT for this type of operation. Instead of manually rearranging keys and maps, it simply uses GroupBy. Furthermore, it uses C under the hood so is way faster. So wny not use it Here?

One word, dependencies. When you have a small chunk of data you want to memorize creatively, you dont want to be spending time importing dependencies for such a light dataset. For huge sets, it is non negotiable. For this kind of project, hand rolled all the way.

## Recent changes:
- The program is a command line utility that expects a clean csv as input. You pipe it in using bash, then voila. You can start interacting with it by specicying keys and flags.
```
cat your.csv | python3 -m main
```
What is this doing? It is taking your printed out csv (your.csv), creating a pipe and feeding it in as input to the python program. What does this mean? No more having to directly link one file at a time, you can pass in whatever and get to work!
