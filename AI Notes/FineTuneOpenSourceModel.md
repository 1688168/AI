# Fine Tune Open Source Model
## LoRA: trick to train enormous
* low rank adapter
  * step 1: freeze the weights - we will not optimize them
  * step 2: select some layers to target, called "Target Modules"
  * step 3: create new "adaptor" matrices with lower dimensions, fewer parameters
  * step 4: Apply these adaptors to the Target Modules to adjust them - and these get trained

* The LLAMA model is too big to train, so we use LoRA

## Three Essential Hyperperameters (try and error)
* R: number of dimension (start with 8 then 16, 32 - power of 2)
* Alpha: scaling factor that multiplies the lower rank matrices (how much you multiply the two LoRA matrics). (twice the value of R)
* Target Modules: which layers of the neural network are adapted.: start by targeting the attention heads
  

## QLora: Quantization LoRA
* Intuition: keep the number of weights but reduce their precision
* huge memory saving
* efficient way to compress neuronetwork 
* Reduce to 8 bits, or even to 4 bits
* technical note 1: 4 bits are interpreted as float, not int
* technical note 2: the adaptor matrices are still 32 bit
* we Quantizing the base model, not LoRA metrics

## Hyper-parameters
> `5 important hyper-parameters for QLoRA`
1. Target modules: which layer to garet (attention)
2. R (Rank, dimension)
3. Alpha (after multiply A,B add to base model)
4. Quantization (reduce precision)
5. Dropout

> `5 Important Hyper-parameters for Training`
1. Epochs (front to back run)
2. Batch Size (num of data points per run - power of 2)
3. Learning Rate (why you don't like learning rate too big - avoid swing to wide)
   1. learning rate scheduler
4. Gradient accumulation
5. Optimizer

> `4 Steps of Training`: Tweaking the parameters of a model based on a training data
1. Forward Pass -> predict the output given inputs
2. Loass Calculation -> How different was the prediction to the ground truth
3. Backward pass -> How should we tweak parameters to do better next time (the "gradients")
4. Optimization -> Update parameters a tiny step to do better next time