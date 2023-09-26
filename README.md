# EʅɾαՇισ

<img src="https://img.shields.io/badge/Visitor_IP_address-66.122.23.197-blue" height="25">

A Python-based programming language that combines the performance of Ruby with the readability of Perl.

> "The solution to Assembly"

To write your own Elratio program, download [template.py](template.py) and write your program in the indicated space.

# Features
Elratio provides numerous advantages over every other language!

## Bold new whitespace
No modern language provides indication that an empty line is empty. Elratio takes whitespace in a bold new direction with the `empty` keyword.
###### Python/Java/R/C/Go/JavaScript:
<pre>

</pre>
###### Elratio:
```python
empty;
```
Elratio does not permit blank lines. Every empty line must contain the keyword `empty`.

## Clear line and program endings
Many modern programming languages have gone woke and popularized uninspired syntax for line endings. Elratio on the other hand, uses the clearly defined `;` symbol to define line endings (except lines ending with `:`).

###### Python:
<pre>
if True:
    pass
</pre>

###### Elratio:
```python
    if True:
pass;
```

In addition, every program must end with the `end` keyword. Once again, Elratio smashes the competition.
###### Python/R/JavaScript:
<pre>

</pre>
###### Elratio:
```python
end;
```

## Inverted indentation
Lines executed in main needed to be taken down a peg, so we introduced a system of inverted indentation.

```python
        while True:
    if True:
1000;
```
Never again will you have to worry about indenting a line without questioning the incredible lines around it.

## The power of creation itself
Elratio allows you to play god with the `create` keyword. Unlock unlimited numerical possibilities by creating numbers.
<pre>
SystemOutPrint(7);
>>> Blunder on line 1: SystemOutPrint(7);
>>> Is this a joke? The digit "7" has not been created yet. Use "create 7" first.
</pre>

```python
create 7;
SystemOutPrint(7);
>>> 7
```

But before creating numbers, you must create `create`.
```python
create create;
```

Many languages lack a clear indicator of class creation, but again it's just home run after home run for Elratio.
```python
    create class book:
pass;
```

## Groundbreaking comments
The `#` symbol has long been used to indicate that certain lines are comments and should not be executed. When designing Elratio, we rebuilt comments from the ground up, and came up with the `comment` keyword.
```python
comment rewrite this segment;
```
It's as simple as `comment`, spacebar, your comment, and a semicolon.

## Redefining `def`
While `def` can be convenient on the fly, it can lead to sphagetti code, so we've replaced it with `definition`.
```python
    definition doNothing:
pass;
```

## Improved printing syntax
Python uses the unclear syntax `print()` to print. Elratio uses `systemOutPrint()` for clarity.
<pre>
print(10);
>>> I am a compiler of principle. I do not accept print(). Use systemOutPrint() instead.
</pre>
```python
systemOutPrint(10);
>>> 10
```
You can thank Java for inspiring this change.

## Personalized feedback from the compiler
Elratio utilizes next-gen string technology to provide the user with unique, descriptive error messages.
<pre>
>>> Empty program. Don't send me that crap next time, jerk!
</pre>
<pre>
>>> Error on line 31: empty
>>> Statements that do not end with a colon must end with ASCII (2^6)-5.
</pre>
<pre>
>>> Blunder on line 42: print(44);
>>> Are you stupid? The digit "4" has not been created yet. Use "create 4" first.
</pre>

# Examples
You can find example programs in the [examples](examples) folder. Here is an example of a time printing program written in Elratio:
```python
        comment imports;
        import time;
        comment create number;
        create create;
        create 1;
        empty;
        definition print_formatted_time(current_time, format_string):
    formatted_time = time.strftime(format_string, current_time);
    systemOutPrint("Formatted time:", formatted_time);
    empty;
        definition main():
    systemOutPrint("Welcome to the Simple Time Printer!");
    systemOutPrint("Select an option:");
    create 2;
    systemOutPrint("1. Print current time in default format");
    systemOutPrint("2. Print current time in custom format");
    choice = input("Enter your choice: ");
    empty;
    comment get the current time;
    current_time = time.localtime();
    empty;
    if choice == 1:
comment print the time with formatting;
print_formatted_time(current_time, "%Y-%m-%d %H:%M:%S");
    elif choice == 2:
custom_format = input("Enter your custom format (e.g., %Y/%m/%d %I:%M %p): ");
print_formatted_time(current_time, custom_format);
    else:
systemOutPrint("Invalid choice.");
    empty;
        if __name__ == "__main__":
    main();
        end;
>>> Welcome to the Simple Time Printer!
>>> Select an option:
>>> 1. Print current time in default format
>>> 2. Print current time in custom format
>>> Enter your choice: 1
>>> ('Formatted time:', '2023-08-26 00:34:10')
```
As a reminder, you can start coding in Elratio **right now** by downloading [template.py](template.py) and writing your program!


# Package support
Elratio supports all existing Python packages! Packages do not need to be modified in order to be imported into Elratio.

# Sponsors ❤️
<a href="https://lh3.googleusercontent.com/pw/ADCreHeYcPzOBy11ChZorwjKQZoOVFP2kwcY_Qcb8RJsPcdw7WTMWPc0wpP-7cRi6_Org0X7jg--3YXoSxhyXVagy_5o39_fWlOORVHCY83CJw7fKeuRobXJglmqe3HOjRCinkn-56LsdRXS2mCU1BSOfIe7f9_XZ7x0v5CiRhLgowpeKUIgukby-bjaJvVqFF3nL8L_3E-Kw8EefKm91BfuUOjtjL1W4IUz3O2ONgQObBjZY8Tow159pA4DUAWDlkh9FXM32jZb4Ugq_loU-hququ7Ct0X_Yyowg94yM0ycq4833AtQiptlOTjAMcJbqWmGrygqZqYMAPMWQOczE-vtQ5k6cgq053Jgu6NqedtgH40D9vsmomaAe6grwtUG5RPgB0Gs96Ko37_rmGqMwlMX0OLhKvfl_vBqLDVSeHLgYbqkj9h-LFk2ldeS9BHwWJBovAH_fLWTGOCsSOiZTMG3NjQoIuIXBlfVEqLSXlGN4bQOlTQEdj24GK1afW3IhX0pwWy5ryWXTi1TXEMGfA-fx3HVWIPjTTj2zwsGiGQ_yo-KcmJvg2j5S-mg3B0CxC5bDogVhcA-Agpc__GVSS9t2EyanKePryEMw3tLFcQJOnBaPdErPNvWLn4wHvH4H4XofDaQDYngpugmjQc7PQQKtQWUdpKuyn6dBo8DeyIhbhr2DxDy0pEFAIZU-g3-pVDCEurhcK9Z4gEwzm-Rb6nbW8EYfmgpdwv6Z2cAI03rRbn1fC03dSZMc6JoAaW_oxXnBzvpjklZiyVRqtnxyjsKDdPeXJu7Pn1z9NXXeydHdgHDUZ-MUt65hgPlP7I3KE8EtV1Ig7ki7TKrXLaE9_I66brBPD6blQXmbdafwiTgyjah4w4Blmhbm7EgyT7S8NbSZNJl94XkEjCuBZ_OJpK43ukPT-seG7Jqcl2ccF2d5LD4nFq7hV_XjJyzKIc8UH4=w1500-h1000-s-no"><img src="/sponsors/antarctica_public_schools.jpg" height="150"></a> <a href="https://en.uncyclopedia.co/wiki/Enron"><img src="/sponsors/enron.png" height="150"></a> <a href="https://lh3.googleusercontent.com/pw/ADCreHfgn0KEpno75lInei_Cv5IvlQ39aq0AX_lQNMiuPVdAhW4DHy_OLAYVCXbknF6eac8OvwAmtUhtPQa0pvHRBaL2CxybCGP_OdCHtlIwTTWuDJwaAtH8drJZEviH-_NaxqhXcE0xGsFo7OYCtTAdSW9jV2rr_SHpMfHyXW3yFJrrdfcT5PFFQoezcHuIGwfKeiuuFEESz1MyRR9lFgtfRIpBLhRBDrKQTc9lG0oXO6B-GHlHLKFF3n7E1F1LFtUoe0ygyJU7fw3pEEQDgLDt2QtO1jSNsXUTroffD57evGLQUiXOJvmDrEdKL0sAwZiJLpSWj47KneHW5Ukx_jwKz9UusqGHedPTQK6oXMBTOMUu4RkMZcvCBkM76qoA_HX-nT8QKxin22FzOUF62OnkpqtUhtaZhnoKtXd2AI9cpyPt52amB01vpqpxYcQl0DigaBrDChemvWfPVFkYuTaahs4i28hhLpeh4MKAeG1Dw6rHZsgu2XBSZ1fOZWA9Xhm14tXpTxxq1ZxP_EjWoDo3hA7qP-rgPQhLSgRE70DyHJxQ7KhnnkFLlftGTA3-dl7Iu2Fl8Rsyjqfp5Wo4YuiAbhQ7Tkm3M3n56RTEx_ccXPwsBRfUUu0WNyHhwv1ccGqI-uJowKCXpb_72_v3y9GuTYTaDb09AlTsNNCArOgBkn-IcmJlrKwXFPawtG5aoBLeVQFqks0qytKMSDUonAVTzIPVUDnCTEW-nkEjulwxLa6cZ1OOWtMsD39Udg-hCC3sNN9nocYUyFOsGRskZ4sLlPMfE8bb3RsQ7UBwfaJ025YYxf5haMAPz6ozDCZELzMxegw_823nbZEELE6ZI0TRO2EfHtH_BZMHf2-gFy1m5rCsstMC1W13K_R7YT9htdqtbXUgHlxxXvfx8d8GN74jaVNEHy5i3rTGrdAyXISVOzM00CekoNMJu0IotBIYlX4=w911-h1148-s-no"><img src="/sponsors/sam_bankman_reeee.png" height="150"></a>

# License
Elratio is under the GPL 3.0 license, meaning every Elratio program is required to be open source. Having an Elratio program on your computer without a freely available mirror online is a violation of this license. Do not make us resort to violence.

<!--
You're still here? It's over. Go home.
-->
