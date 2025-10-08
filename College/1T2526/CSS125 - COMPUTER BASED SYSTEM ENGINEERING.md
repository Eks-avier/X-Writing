# CSS125 - COMPUTER BASED SYSTEM ENGINEERING

> [!IMPORTANT] TOPICS COVERED
> * Emergent system properties
> * Systems and their environment
> * System modelling
> * The system engineering process
> * System procurement

## SYSTEMS ENGINEERING

* **Designing**, **implementing**, and **deploying** operating systems which include hardware, software, and people.

## What is a system?

- It is a collection of *inter-related* components working *together* towards some *common objective* that is *purposeful*.
- It can be *operated by people* and includes:
	- Software
	- Mechanical
	- Electrical
	- Electronic Hardware
- System components are *dependent on each other*.
- The properties and behavior of system components are *inextricably* inter-mingled.

## PROBLEMS OF SYSTEMS ENGINEERING

- Large systems are usually designed to solve *wicked* problems.
- Systems engineering requires a great deal of *coordination* across disciplines.
	- There are almost *infinite* possibilities for *design trade-offs* across components.
	- *Mutual distrust* and *lack of understanding* across engineering disciplines.
- Systems must be designed to last *many years* in a *changing environment*.

## SOFTWARE AND SYSTEMS ENGINEERING

- The proportion of software in systems is increasing. Software-driven *general purpose* electronics is replacing *special-purpose* systems.
- Problems of systems ENGINEERING are similar to problems of software engineering.
- Unfortunately, software is seen as a problem in systems engineering. Many large system projects have been delayed because of software problems.

## EMERGENT PROPERTIES

- Properties of the system as a whole rather than properties that can be derived from the properties of the components of a system.
- Emergent properties are a consequence of the relationships between system components.
- They can therefore only be assessed and measured once the components have been integrated into a system.


> [!EXAMPLE] Examples of Emergent Properties
> - **The Overall Weight of the System**: It can be computed from individual component properties.
> - **The Reliability of the System**: This depends on the reliability and relationships between the system components.
> - **The Usability of a System**: This is a complex property which is not simply dependent on system hardware and software but also on the system operators and the environment where it is used.

### TYPES OF EMERGENT PROPERTIES

- **Functional Properties**: They emerge from the collaboration of the system parts to achieve some objective. 
	- **Example**: A bicycle has the functional property of being a transformation device once it has been assembled from its components.
- **Non-functional Emergent Properties**: Relating to the behavior of the system in its operational environment, they are critical for computer-based systems as failure to achieve some minimal defined level in these properties may make the system unusable.
	- **Example(s): 
		- Reliability
		- Performance
		- Safety
		- Security

## SYSTEM RELIABILITY ENGINEERING

- Because of component inter-dependence, faults can be propagated through the system.
- System failures often occur because of unforeseen inter-relationships between components.
- It is probably impossible to anticipate all possible component relationships.
- Software reliability measures may give a false picture of the system reliability.

### INFLUENCES ON RELIABILITY

- **Hardware Reliability**: "What is the probability of a hardware component failing and how long does it take to repair that component." 
- **Software Reliability**: "How likely is it that a software component will produce an incorrect output. "
- **Operator Reliability**: