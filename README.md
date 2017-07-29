# AutoPerf #
### What is AutoPerf? ###
Autoperf is a tool for automated diagnosis of performance anomalies in multithreaded programs. It operates in two phases:
1. Profiling: Collect hardware performance counters from "annotated" sections of a progam by running it with performance representative inputs.
2. Anomaly Detection: Create a model of application performance behavior by training an [Autoencoder](http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/) network. Use profiling dataset as training data for input. Then, use the trained model for anomaly detection in future executions of the program.


### How to run? ###
* Profiling:
  * Autoperf uses [PAPI](http://icl.cs.utk.edu/papi/index.html) interface for performance counters. Extract and install from source (papi-5.5.1.tar.gz)
  * Build profiler library:
    * cd AutoPerf/proflier 
    * make
  * Prepare candidate "program":
    * Annotate functions: 
      * add header : `#include "perfpoint.h"`
      * mark start : `perfpoint_START(marker_id)`
      * mark end : `perfpoint_END(marker_id)`
      NOTE: use mark_id as parameter to uniquely identify code region
    * Link profiler library `libperfpoint.so` with candidate "program" or use LD_PRELOAD=/path/to/libperfpoint.so (example: Default.mk in tests dir)
  * Run program :
    * create list of perforimance counter names in file named "COUNTERS" in binary path [ or copy the file Autoperf/profiler/COUNTERS]
    * copy Autoperf/profiler/run_test.py in banary path
    * `python run_test.py PROGRAM_BINARY PROGRAM_ARGS PATH/TO/OUTPUT/PROFILE_DATA`
* Anomaly Detection:
  * Requirements: Python 2.7+, [keras](https://keras.io/) library
  * `cd AutoPerf/Trainer`
  * set `NUMBER_OF_COUNTERS` and `NO_OF_HIDDEN_LAYER_TO_SEARCH` in `configs.py`
  * `python autoencoder.py PATH/TO/PROFILE_DATA_FOR_TRAINING PATH/TO/PROFILE_DATA_FOR_TEST PATH/TO/OUTPUT_DETECTION_RESULTS`







