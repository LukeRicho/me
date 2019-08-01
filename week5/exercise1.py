# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    start = 7
    stop = 0
    message = "Commencing in {}"
    last_message = "We have lift off"
    
    while True:
        print("{m} {n}".format(m=message, n=start))
        start = (start - 1)
        if start == stop:
            break
        print(last_message)
        return last_message


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = (base**2 + height**2)**(1/2)
    return(hypotenuse)


def calculate_area(base, height):
    area = (base*height)/2
    return(area)


def calculate_perimeter(base, height):
    return base + height + calculate_hypotenuse(base, height)


def calculate_aspect(base, height):
    if base > height:
        return "wide"
    elif base < height:
        return "tall"
    elif base == height:
        return "equal"
    

# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    facts = pattern.format(**facts_dictionary)

#compares base and height to find the aspect
    if "base" > "height":
        Aspect = wide
    elif "base" < "height":
        Aspect = tall
    elif "base" == "height":
        Aspect = equal

    return Aspect + facts

def triangle_master(base, height, return_diagram=False, return_dictionary=False):

    facts = get_triangle_facts(base, height)
    diagram = tell_me_about_this_right_triangle(facts)

    if return_diagram and return_dictionary:
        return diagram and facts
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return facts
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid(api_key):
    import requests

    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?"
        "wordlength={length}"
    )
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.text
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    for i in range(20, 3, -2):
        url = baseURL.format(length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.text
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    return pyramid_list


def get_a_word_of_length_n(length):
    
    import requests

    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?"
        "wordlength={length}"
    )
    l = length
    limit = 0
    list1 = []
    for length in range(limit):
        url = baseURL.format(length = l)
        r = requests.get(url)
        if r.status_code is 200:
            text = r.text
            list1.append(text)
            if type(text) == str:
                return ("\n".join(list1))
            else:
                return None


def list_of_words_with_lengths(list_of_lengths):
    
    import requests

    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?"
        "wordlength={length}"
    )
    word_list = []
    for x in range(3, 21, 2):
        url = baseURL.format(length=list_of_lengths)
        r = requests.get(url)
        if r.status_code is 200:
            text = r.text
            word_list.append(text)
        else:
            print("failed a request", r.status_code, x)
    return word_list


#if __name__ == "__main__":
    #do_bunch_of_bad_things()
    #wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
