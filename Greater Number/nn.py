import random

for i in range(0, 1000):
	weight = [[random.uniform(0, 1),random.uniform(0, 1)],[random.uniform(0, 1),random.uniform(0, 1)]]

	def neuralNetwork(input1, input2):

		output1 = input1*weight[0][0] + input2*weight[1][0]
		output2 = input1*weight[0][1] + input2*weight[1][1]

		output1 = sigmoid(output1)
		output2 = sigmoid(output2)

		sumofoutputs = output1+output2

		output1 = output1/sumofoutputs
		output2 = output2/sumofoutputs

		return[output1, output2]


	def backPropagation(input1, input2, output1, output2):

		truevalue1 = 1 if input1 > input2 else 0
		truevalue2 = 1 - truevalue1

		error1 = truevalue1 - output1
		error2 = truevalue2 - output2

		weight[0][0] += error1*input1
		weight[1][0] += error1*input2
		weight[0][1] += error2*input1
		weight[1][1] += error2*input2



	def sigmoid(a):
		if a<0:
			return 0
		return a

	lastwrongiteration = 'did not converge'
	for i in range(0, 10000):
	
		input1 = random.randint(1, 10)
		input2 = random.randint(1, 10)
		# print('================')
		# print('input 1: ', input1)
		# print('input 2: ', input2)
		# print('iteration: ', i)
		result = neuralNetwork(input1, input2)
		# print('result', result)
		# print('weight 1', weight)
		backPropagation(input1, input2, result[0], result[1])
		# print('weight 2', weight)
		if ((input1-input2)*(result[0]-result[1]))<0:
			lastwrongiteration = i

	print(lastwrongiteration)
	#print('weight 2', weight)

		# if result[0] == 0.0:
		# 	print('became ideal in: ', i)
		# 	break

	# print('end')
