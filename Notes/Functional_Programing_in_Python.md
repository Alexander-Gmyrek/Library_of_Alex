# Functional Programing in Python

Created: June 8, 2024 5:56 PM

## Quick Notes

- Lambda stuff: One of the concepts from functional programming is passing one function into another broader function. From that you get the idea of “currying” where instead of handling the entire operation at once it instead Returns a function that handles the next part of the operation. The later part has the previous state “bound” to it and the new on the fly created function is what gets called when we want to check a condition. So instead of binding function to an object you bind objects to a function. Labda is the next step and basically allows you to simplify and chain these together to basically create a data pipeline out of “fundamental functions” like map, filter, slice, or take. In functional programming, “fundamental functions” are often referred to as “higher-order functions” or “functional programming primitives.”

## What is Functional Programing?

Functional programming is basically programming using only functions with no changing state. This means that for any given input you get the same output every time. This is in contrast to Object Oriented Programing. So instead of binding function to an object you bind objects to a function. This is what python was designed around and is why it can feel like objects were an after thought and it is missing some obvious features despite how good it is otherwise.

## Good content:

https://www.youtube.com/watch?v=C2w45qRc3aU (Not me)

https://www.youtube.com/watch?v=nuML9SmdbJ4