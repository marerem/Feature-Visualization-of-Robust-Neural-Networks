# Meeting notes and todo for the following week

## Week 1
### todo
- Refresh on Robust Neural networks
- Read https://distill.pub/2017/feature-visualization/
- Do Lucent tutorial : https://colab.research.google.com/github/greentfrapp/lucent-notebooks/blob/master/notebooks/tutorial.ipynb


## Week 2
- Research question: What/Where is the visual difference in terms of Feature Visualization between a normal and a robust NN?
- neurons/layers between robsut and normal look similar, 
- 1st step: find sensitive neurons,
- after... we'll see
- on the network resnet34
### todo
- LR adversarial attack (we don't care about the improving part)
- Lucent, choose a neuron and try to attack it

## Week 3
- Project plan ?

# Week 4
- visualize as video instead of last step
- parametrize with CPPN
- create adversarial attacks find sensitive neurons
	- undirected adversarial attack
	- feed same image twice (1 attack and 1 normal)
	- see which channel changes the most
	- take validation set of ImageNet as dataset
	- visualize those neurons

# Week 5
- Implement adversarial attack and find sensitive neurons
	- Use FGSM attack (or iterative mehod if not good enough)
	- Use perturbation of the model to test sensitivity (no need to test from the other's perturbation)
	- Tweak parameters of the attack until normal model around 50% accuracy
	- Need to find what neurons and how sensitive it is
	- Compare sensitivities and if the same neurons are sensitive
	- Neuron sensitivity paper : https://arxiv.org/pdf/1909.06978.pdf
	- FGSM attack : https://medium.com/onfido-tech/adversarial-attacks-and-defences-for-convolutional-neural-networks-66915ece52e7
	- Torch attack tutorial : https://pytorch.org/tutorials/beginner/fgsm_tutorial.html
- Visualization
	- Show with and without CPPN parametrization
	- Show layers / neurons that are sensitive
	- Compare robust and non-robust

	# Week 8 
	- Feature extraction : https://stackoverflow.com/questions/52796121/how-to-get-the-output-from-a-specific-layer-from-a-pytorch-model
