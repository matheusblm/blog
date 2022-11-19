How create new controllers in the application.
Create dynamic contenct on controller and display.
Link pages together.

Model view controller is a type of architure

Model is like a gatekeeper and data store.
View generate a user interface.
Controller receive envents interact with the model and display to the view user.

ntroduction To Ruby Languague

Ruby is a Object-Oriented Language

Ruby name - Start with lowecase and use underline.
Instance variable begin with a @
Class Name, module names, and constants must start with an uppercase.
Rials use symbols to identify things, uses them as keys when naming method parameters and looking thing up in hashses.

Methods =
def say_goodnight(name)
result = 'Good night, ' + name
return result
end

the return keyword is optional, and if it's not present will return the last expression evaluated.
Interpoleation in ruby = "Good nigh, #{name.capitalize}"

The << () mehotd it appends a single value to its receiver

Example of a Hashes
inst_section = {
:cello => 'string',
:clarinet => 'woodwind',
:drum => 'percussion',
:oboe => 'woodwind',
:trumpet => 'brass',
:violin=> 'string'
}

Logic -

Methods calls are statemetns.
Blocks are bettewen do and ned ou {}
Example of a methods if a block
greet { puts "Hi" }

animal.each {|animal| puts animal}
3.times {print "Ho! "}

### Organizing Structures

Ruby has to basics concepts for organizing methods: classes and modules.

#### Classes

class Order < ApplicationRecord
has_many :line_items
def self.find_all_unpaid
self.where("paid = 0 ")
end
def total
sum = 0
line_items.each {|li| sum += li.total}
sum
end
end

class Greeter
def initialize(name)
@name = name
end
def name
@name
end
def name=(new_name)
@name = new_name
end
end

private on up of the name methods make him private, that is only the instance of this class can call this method.

### Module

Modules are similiar to classes, but they are use to create another classes base on modules.
A great example is Helper methods.

module StoreHelper
def capitalize_words(string)
string.split(' ').map {|word| word.capitalize}.join(' ')
end
end

### Marshaling Objects

Ruby can take an obkect and conver it into a stream of bytes that can be stored outsid the appitcatioon.

Rubt uses marshaling to store session data.

### Ruby Idioms

Methods such as empty! and empty? - bang methods do something destructive to the revicer !, and ? method return true or false.

a || b - evalutes If it isnt flase or nill
