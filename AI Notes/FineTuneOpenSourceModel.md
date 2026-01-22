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