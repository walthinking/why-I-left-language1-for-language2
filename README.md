# Overview

Origin idea from [Why I Left Language1 For Language2](https://medium.com/@igorhorst/why-i-left-language-1-for-language-2-1d2fa418cd4c#.jn9fhmhn8).

[![Build Status](https://travis-ci.org/qiajigou/why-I-left-language1-for-language2.svg?branch=master)](https://travis-ci.org/qiajigou/why-I-left-language1-for-language2) [![Join the chat at https://gitter.im/qiajigou](https://badges.gitter.im/qiajigou.svg)](https://gitter.im/qiajigou?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


# Run Online

Visit [http://why.qiajigou.click](http://why.qiajigou.click) to run this program online. :)

# Install

Init submodule

```
git submodule init
git submodule update
```

These commands will checkout the hello-world folder.

Just checkout this project and run.

```
make && ./wuliao
```

Or

```
make install
```

# wuliao(1)

Yes! We are so boring that we wrote this project by C, this is really... I don't know what to say but I am not the one who good at C.

OK, Just enjoy yourself!

```
wuliao -1 Java -2 Python -3 Python3
```

Add your templates!

```
wuliao -1 Java -2 Python -3 Python3 -t templates/en/justno.md -w hello-world/
```

**TIPS**: You can make this project yourself!

# Help

```
Why I left language1 for language2

-0  -0 C -> Language that you was used bug gived up
-1  -1 Java -> Language that you used but gona leave this
-2  -2 Python -> Language that you are going to use and love this
-3  -3 Python3 -> If language2 you don't like, there still a chance
-t  -t template_path -> Customized template path
-p  -p Tomecat -> Project you was working on with language1
-w  -w Set hello-world folder path
-h  -h Show this help

Example: ./wuliao -1 Java -2 Python -3 Python3 -t templates/en/justno.md
:)
```

# Python

There is a Python implementation so you can use it on web (or like a toy). This is simple and easy.

```
python wuliao.py -1=Java -2=Python -3=Python3
```

Add your templates!

```
python wuliao.py -1=Java -2=Python -t=templates/en/justno.md
```

Get more help by using:

```
python wuliao.py --help
```

# Output

I am a big fan of Java and one of its early adopters, having been disappointed with the utter failures of C. I have been an avid contributor to many open source projects such as Spring MVC, Tomcat. However, after using Java for over 5 years, I have been dealing with minor technical flaws. At first, I ignored and even tolerated these flaws, but ultimately, I was forced to confront reality. I could not live with these flaws, and since Java is a mature language, it will be difficult, if not impossible, to actually fix these flaws.

I also resented the opinions that Java took. When I first used those languages, I thought those opinions were a fresh breath of air. I would constantly defend those opinions on Hacker News, because I thought that these opinions would promote good coding practices and would ulitmately lead to higher productivity. After 5 years of coding though, I realized that those opinions may have been slightly flawed.

And then, I heard of Python. Python promised to fix all the technical flaws in Java. I also read about the opinions inherent in Python, and realized that those opinions were utterly correct, compared to the fallicious and wrong-headed opinions in Java. And that’s why I switched languages.

Let me show you an example to prove my point.

Here is an example of a “Hello World” program in Java:

```Java

public class Java {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}

```

You can see why I was drawn to this language. Its syntatic sugar was beautiful. But it was ultimately too magical. I didn’t know what was actually going on. What did Format mean? Or Write? When I had to scale up my program, I would be cursing all night trying to debug the latest ‘magic’ that Java decided to invoke on me. Half the time, I would be fighting against Java’s constraining limits.

And here’s an example of “Hello World” in Python:

```Python

#!/usr/bin/env python
print "Hello World"

```

You can see how easily readable and maintainable Python is over Java. Its syntax is just as elegant as Java, but there’s no magic involved. Everything that I need to know is right there, ready to be understood in an easy-to-digest fashion. There’s no fighting with the language here, just me working with my trusty new tool.

Always use the best tool for the job. That’s why I have chosen to use Python for all my obscure side-projects. It will likely not have any technical flaws whatsoever, nor will its opinions ever turn out to be wrong. And, in the rare case that Python disappoints me…well, there’s always Python3…

# Contribute

Do you want a website for this projects?

Feel free to give PR. :D
