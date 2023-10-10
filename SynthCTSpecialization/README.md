# Patches for SynthCTSpecialization

This folder contains configuration and regression patches for the `SynthCTSpecialization` project.

## General

The SynthCTSoecialization project exposes 2 configuration options that can be switched:

- Storage
    - DefaultStorage -- A default implementation using only the feature Storage`
    - CachableStorage -- An emulation for a storage that uses caching. Exposes an interaction between `Storage` and `Cache` features
    - BoundsCheckingStorage -- An emulation of a storage that check bounds on access. Exposes an interaction between `Storage` and `BoundsCheck`
- Algorithm
    - DefaultAlgorithm -- A default transformer only using the feature `Algorithm`
    - SmoothingAlgorithm -- A smoothing algorithm that exposes an interaction between `Algorithm` and `Smoother`
    - DirectSolvingAlgorithm -- An alternative algorithm implementation that directly exposes a `solve` function.
## Configuration Patches

There are configuration patches for the whole configuration spaces available. The `feature_tags` of the info files will contain the names of the configuration options that are activated

A configuration patch is of the form `$AlgoTy_$StorageTy.patch` where `$AlgoTy` and `$StorageTy` are shorthands of the activated configuration option for that category.

## Regression Patches

For each configuration option one or multiple regression patches of 5 severities (`1ms`, `10ms`, `100ms`, `1000ms` and `10000ms`) are available.
The `tags` in the `.info` file will contain the name of the confugration option that is affected. Artificial regressions will be introduced into a specific function in the source code.
Both the regressed function and the severity are indicated in the file name.

TODO: Overview of affected feature regions per regression (?)