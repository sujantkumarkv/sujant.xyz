+++
title = 'timeseries transformers'
date = 2024-05-23T00:00:00Z
draft = false
+++

> i discuss my college project on using deep learning (notably, transformers' flavours) for prediction of streamflow of river stream (here, hemavathi basin).

the project involves rainfall, river streamflow & temperature data for the study area: hemavathi basin, kaveri river, karnataka, india. 
![hemavathi_basin](/assets/timeseries/hemavathi_basin.webp)
thanks to phd senior `mukul sahu` for arranging the data from India Metrological Department (IMD). The data consisted of daily data points from `2003-2020` with a total of `6575 rows` each.

![data.webp](/assets/timeseries/data.webp)
![discharge_data.webp](/assets/timeseries/discharge_data.webp)
![waterlevel_data.webp](/assets/timeseries/waterlevel_data.webp)

mostly traditional machine/deep learning techniques are used in this niche space of hydrology. he had some experience with Lstm & Cnn but i proposed that attention based transformers shall be explored and i started working on it. my friend [`nihal badiger`](https://www.linkedin.com/in/nihal-badiger-a53a61196/) trained xgboost & Lstm models. i was exploring on how to best make timeseries data work with transformers. the work includes around 1month of worktime, and may see more progress before its published.

*as a result, this page will probably be updated in the future.*

the intuition is to use timestamps as positional encodings as its used in language modelling. i built encoder-decoder vanilla transformer and also use [`LagLlama`](https://arxiv.org/abs/2310.08278) which is trained on timeseries with llama architecture. I also read a chinese paper doing something similar with yangtze river [`Liu et al., 2022`](https://www.researchgate.net/publication/361160854_Improved_Transformer_Model_for_Enhanced_Monthly_Streamflow_Predictions_of_the_Yangtze_River) where they modify the transformer architecture to fit their data, we had different data than them though. Another interesting paper which introduces [`spacetimeformer`](https://arxiv.org/abs/2109.12218) concept of spatio-temporal transformers for multivariate timeseries data (yet to be tested for this project)


- vanilla encoder-decoder based model

It's a ~60M parameter model trained on 10 epochs over the multivariate data of average temperature, waterlevel, streamflow & a generated lag feature: streamflow_lag_1. find relevant code, [`here`](https://github.com/sujantkumarkv/timeseries-transformers/tree/main/encoderdecoder).

![data.csv.webp](/assets/timeseries/data.csv.webp)

overview of the model, model configurations and validation scores.

[![encoderdecoder_stats.webp](/assets/timeseries/encoderdecoder_stats.webp)](https://x.com/sujantkumarkv/status/1775881363373388243)

the biggest pain i had to bear was digging deep into [`gluonts`](https://github.com/awslabs/gluonts) libary by amazon which is used for data processing & handling in both examples. 

![data_proc_pain.webp](/assets/timeseries/data_proc_pain.webp)

the [`huggingface example blog`](https://huggingface.co/blog/time-series-transformers) consists of a decoder-only model with a probablistic head & uses [`monash_tsf`](https://huggingface.co/datasets/monash_tsf/viewer/tourism_monthly) dataset for timeseries which was very confusing as to what does the data points represent & in which order.

- latest foundation model called `LagLlama`, based on the Llama architecture from Meta but trained specifically on huge amounts of time-series data which has been used with zero-shot and fine-tuned upon our datasets to further improve the quality of results. 

here's the zeroshot discharge/streamflow predictions, it does impressively well for its size:

![lagllama.zeroshot.webp](/assets/timeseries/lagllama.zeroshot.webp)

Further, we finetune the 2.4M parameter lagllama model.

![lagllama.webp](/assets/timeseries/lagllama.webp)

I trained it for `50 epochs on a Nvidia T4 GPU` freely available in google colab & other online services like lightning studios.

![lagllama.ft.webp](/assets/timeseries/lagllama.ft.webp)

here's lagllama github repo. it contains more details & notebooks released by the team.
[`lagllama`](https://github.com/time-series-foundation-models/lag-llama).

*what's next: more updates may involve testing: amazon's cronos model, timegpt, spacetimeformer (spatio-temporal), decoder-only transformer.* 