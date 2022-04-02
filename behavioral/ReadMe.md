# Chain of Responsibility pattern

Chain of Responsibility pattern example provides simple example of usage Buff/Debuffs system. In the example are provided 3 types of Buffs and Debuffs. The example only gives an idea, but is not a full implementation of Buff/Debuff system.

To run example, you simply need to run:

> [chain_of_responsibility_main.py](chain_of_responsibility/chain_of_responsibility_main.py)

# Command pattern

Command pattern example demonstrates usage in trading system between player and merchant. Both player and merchant have some items to sell as well as some limited amount of money, who knows maybe one day you won't be able to buy something until you sell some of your stuff.

The example is probably the most interactive among all provided. You can both sell and buy items, every trading might be considered as unique, because trader's Gold, items and their price are generated randomly.

To run example, you simply need to run:

> [command_main.py](command/command_main.py)

# Interpreter pattern

Interpreter pattern example provides very simple interpreter of addition and subtraction operations with integers.

To run example, you simply need to run:

> [interpreter_main.py](interpreter/interpreter_main.py)

# Iterator pattern

Iterator pattern example provides solution for iterating Binary Tree graphs. There are two iterators: Breadth-First Search and Depth-First Search.

To run example, you simply need to run:

> [iterator_main.py](iterator/iterator_main.py)

# Mediator pattern

Mediator pattern implementation demonstrates conceptual example of Air Alarm Service (Unfortunately this is first thing that came into my mind due to ongoing russian war against Ukraine). People can subscribe to Air Alarm Service using mediator and Air Alarm Service can publish to People using mediator as well.  

While it's simple example, here could be added more features like: unsubscribe and change the city, but these features are easy to implement, so if anyone wants to update example they might try on their own.

To run example, you simply need to run:

> [mediator_main.py](mediator/mediator_main.py)

# Memento pattern

Memento pattern example demonstrates its usage for saving in-game progress of player and restoring data from one of the snapshots.

To run example, you simply need to run:

> [memento_main.py](memento/memento_main.py)

# Observer pattern

Observer pattern example demonstrates conceptual example of Newsletter system with subscription and unsubscription mechanism. User defines what topics he is interested in and receives newsletters in case published news article's topics contain at least one topic that user subscribed.

To run example, you simply need to run:

> [observer_main.py](observer/observer_main.py)

# State pattern

State pattern example demonstrates usage of state-machine based on conceptual example of Ticket (such as JIRA system has). Particular states can be transitioned only to other particular states, see the table below.

| \             | Open          | In Progress   | Resolved      | Closed        |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| Open          | -             | +             | +             | -             |
| In Progress   | +             | -             | +             | -             |
| Resolved      | +             | -             | -             | +             |
| Closed        | +             | -             | -             | -             |

To run example, you simply need to run:

> [state_main.py](state/state_main.py)

# Strategy pattern

Strategy pattern example demonstrates very primitive usage of Strategy pattern by providing different representations of object such as XML and JSON. In this demo there are no additional logic on high-level class that operates with Strategies, but basically in most cases high-level class also has additional logic to further process data etc.

To run example, you simply need to run:

> [strategy_main.py](strategy/strategy_main.py)

# Template Method pattern

Template Method pattern example demonstrates its usage based on file reading. First template read data from local source, second template read raw data from URL. Both of them are inherited and use shared methods from parent template class.

To run example, you simply need to run:

> [template_method_main.py](template_method/template_method_main.py)

# Visitor pattern

Visitor pattern example provides demonstration on how can be applied additional operations with objects with minimal objects modification. In the example objects are converted to TXT, XML and JSON formats by using Visitor pattern approach and then saved into files. 

To run example, you simply need to run:

> [visitor_main.py](visitor/visitor_main.py)
