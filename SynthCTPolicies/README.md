# Patches for SynthCTPolicies

This folder contains configuration and regression patches for the `SynthCTPolicies` project.

## General

The SynthCTPolicies project exposes 3 configuration options that can be switched using different policies:
- Logging
  - DevNullLogger -- The default logger that does nothing
  - ExpensiveLogger -- A simulation for an expensive logger that emulates a long running log operation
  - DataBaseLogger -- An emulation for a logger that writes to a database. This exposes an additional interaction between the `Logging` and `DataBase` features.
- Storage
  - DefaultStoragePolicy -- A default implementation using only the feature Storage`
  - CachingStoragePolicy -- An emulation for a storage that uses caching. Exposes an interaction between `Storage` and `Cache` features
- Transformer
  - DefaultTransformerPolicy -- A default transformer only using the feature `Transformer`
  - SmoothingTransformerPolicy -- A smoothing transformer that exposes an interaction between `Transformer` and `Smoother`
## Configuration Patches

There are configuration patches for the whole configuration spaces available. The `feature_tags` of the info files will contain the names of the configuration options that are activated

A configuration patch is of the form `$TransformerTy_$StorageTy_$LoggerTy.patch` where `$TransformerTy`, `$StorageTy` and `$LoggerTy` are shorthands of the activated configuration option for that category.

## Regression Patches

For each configuration option one or multiple regression patches of 5 severities (`1ms`, `10ms`, `100ms`, `1000ms` and `10000ms`) are available.
The `tags` in the `.info` file will contain the name of the confugration option that is affected. Artificial regressions will be introduced into a specific function in the source code.
Both the regressed function and the severity are indicated in the file name.

TODO: Overview of affected feature regions per regression (?)
