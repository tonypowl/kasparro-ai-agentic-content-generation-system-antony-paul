# Problem Statement
To create a modular agentic automation system that takes a small product dataset and automatically generates structured content. The goal was to create independent agents that do specific tasks like parsing, generating categorized questions following certain predefined templates and reusable content logic blocks that finally output JSON code in 3 seperate pages. 

# Solution Overview
Based on the requirements, a multi-agent workflow is mandatory so I decided to use 4 agents namely - a control agent, parsing agent, content agent, page format agent that transorm raw product data into structured JSON pages. Creating seperate logic blocks that are essentially simple callable functions, templates are created for the desired output to maintain a consistent structure.

# Scopes & Assumptions
1. Only the product dataset given in the assignment is used.
2. Seperate agent classes have specific tasks/responsibilities that they must carry.
3. Logic blocks are reusable in a sense that they can be used all kinds of similar data.
4. Output follows a certain template and is structured JSON generated in 3 'pages'.

**# System Design**
## Agent Architecture 
Each agent has a single responsibility and explicit input & output
Control agent to coordinate execution flow, called in main.py to tripper the pipeline. 
Parsing agent normalizes the raw data and outputs a clean product model that's more machine friendly.
Content agent is assigned with the task to generate questions and logical outputs.
Page format agent applys a predefined template and ensure that the results are in JSON format and  stored in the 'outputs\' folder 

## Reusable Logic Blocks
- generate_benefits
- extract_usage
- compare_prices

## Templates
- FAQ Template
- Product Description Template
- Comparison Template

## Output Format
All outputs are generated as machine-readable JSON files.



