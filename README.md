# Small Vision Language Model - Image Text to Code

This project provides a benchmark for evaluating multimodal models in the task of code generation from graphical representations, using datasets from Human-Eval and PSB2.

## Project Structure
```
project/
├── data/human_eval				# Data folder
│   ├── p084/               	# Specific single problem
│	│   ├── block/
│	│	│   ├── l1.drawio  		# Block diagram level 1 drawio
│	│	│   ├── l1.drawio.png  	# Block diagram level 1 drawio
│	│   ├── bpmn/
│	│	│   ├── l1.drawio  		# BPMN diagram level 1 drawio
│	│	│   ├── l1.drawio.png  	# BPMN diagram level 1 drawio
│	│	│   ├── l2.drawio  		# BPMN diagram level 2 drawio
│	│	│   ├── l2.drawio.png  	# BPMN diagram level 2 drawio
│	│	│   ├── l3.drawio  		# BPMN diagram level 3 drawio
│	│	│   ├── l3.drawio.png  	# BPMN diagram level 3 drawio
│	│   ├── fc/
│	│	│   ├── l1.drawio  		# FC diagram level 1 drawio
│	│	│   ├── l1.drawio.png  	# FC diagram level 1 drawio
│	│	│   ├── l2.drawio  		# FC diagram level 2 drawio
│	│	│   ├── l2.drawio.png  	# FC diagram level 2 drawio
│	│	│   ├── l3.drawio  		# FC diagram level 3 drawio
│	│	│   ├── l3.drawio.png  	# FC diagram level 3 drawio
│ 	+
├── models/						# Models Information (technical report)
├── problems/					# Problems Information (definition, solution, original and official test cases)
├── results/human_eval			# Results obtained
├── src/
│   ├── core/               	# Core functionality (model management, code execution, GPU utilities)
│   ├── ui/                 	# Gradio interface and styles
│   ├── utils/              	# Shared constants and utilities
├── main.py                 	# Application entry point
├── css/                    	# Custom CSS for Gradio interface
├── requirements.txt        	# Project dependencies
└── README.md               	# Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```


### Human Eval Selected Problems

The Code LLama and GPT-4 evaluation are reported [here](https://github.com/jamesmurdza/humaneval-results/tree/main).

<table>
	<tr>
		<th>Task</th>
		<th width="100">Code Llama</th>
		<th width="100">GPT-4</th>
		<th>Description</th>
		<th>Flowcharts</th>
		<th>BPMN</th>
		<th>Block</th>
		<th>Others</th>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p084/p084.md">HumanEval/84</a></td>
		<td>$$\Large\mathbf{\color{orange}20\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Return the total sum of the digits of a positive integer in binary form.</td>
		<td><a href="data/human eval/p084/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p084/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p084/diagrams/block">Block</a></td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p106/p106.md">HumanEval/106</a></td>
		<td>$$\Large\mathbf{\color{yellow}80\%}$$</td>
		<td>$$\Large\mathbf{\color{orange}30\%}$$</td>
		<td>Calculate and return a list of size n, where each element at index i is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise.</td>
		<td><a href="data/human eval/p106/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p106/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p106/diagrams/block">Block</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p108/p108.md">HumanEval/108</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{orange}10\%}$$</td>
		<td>Count the number of elements in the array that have a sum of digits greater than 0.</td>
		<td><a href="data/human eval/p108/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p108/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p108/diagrams/block">Block</a></td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p119/p119.md">HumanEval/119</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{orange}40\%}$$</td>
		<td>Check if it is possible to concatenate two strings of parentheses in some order to create a balanced string.</td>
		<td><a href="data/human eval/p119/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p119/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p119/diagrams/p119/block">Block</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p120/p120.md">HumanEval/120</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Return a sorted list of the maximum k numbers in the given array.</td>
		<td><a href="data/human eval/p120/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p120/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p120/diagrams/block">Block</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p126/p126.md">HumanEval/126</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{yellow}50\%}$$</td>
		<td>Check if a given list of numbers is sorted in ascending order and does not contain more than one duplicate of the same number.</td>
		<td><a href="data/human eval/p126/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p126/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p126/diagrams/block">Block</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p131/p131.md">HumanEval/p131</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{green}100\%}$$</td>
		<td>Return the product of the odd digits in a given positive integer, or 0 if all digits are even.</td>
		<td><a href="data/human eval/p131/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p131/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p131/diagrams/block">Block</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p147/p147.md">HumanEval/147</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Calculate the number of triples in an array where the sum of the elements is a multiple of 3.</td>
		<td><a href="data/human eval/p147/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p147/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p147/diagrams/block">Block</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p150/p150.md">HumanEval/150</a></td>
		<td>$$\Large\mathbf{\color{green}100\%}$$</td>
		<td>$$\Large\mathbf{\color{green}100\%}$$</td>
		<td>Return the value of x if n is a prime number and return the value of y otherwise.</td>
		<td><a href="data/human eval/p150/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p150/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p150/diagrams/block">Block</a></td>
	</tr>
	<tr>
		<td><a href="./data/human eval/problems/p155/p155.md">HumanEval/155</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Return a tuple containing the count of even and odd digits in the given integer.</td>
		<td><a href="data/human eval/p155/diagrams/fc">Flowcharts</a></td>
		<td><a href="data/human eval/p155/diagrams/bpmn">BPMN</a></td>
		<td><a href="data/human eval/p155/diagrams/block">Block</a></td>
	</tr>
</table>