# Patches for SynthCTTraitBased

This folder contains configuration and regression patches for the `SynthCTTraitBased` project.

## General

The SynthCTTraitBased project is a very bare-bone and artificial example.
It only exposes some arbitrary inspecific features `A`, `B`, `C`, `D`.

In the example, `A` and `B` are features that may be used in a algorithm type, while `C` and `D` are used by a storage type.

The SynthCTTraitBased project exposes 2 configuration options that can be switched:

- Algorithm
    - AlgorithmWithA -- An algorithm that uses feature `A`
    - OtherAlgorithmWithA -- Another algorithm that uses feature `A` and exposes additional interactions to `C` and `D` if these are sued by the storage
    - AlgorithmWithB -- An algorithm that uses feature `B`
    - AlgorithmWithAB -- An algorithm that uses feature `B` and `A`
- Storage
    - StorageWithC -- A Storage type that uses feature `C`
    - OtherStorageWithC -- A Storage type that uses feature `C`
    - StorageWithD -- A Storage type that uses feature `D`
    - StorageWithCD -- A Storage type that uses feature `C` and `D` and exposes an interaction between them,
    
## Configuration Patches

There are configuration patches for the whole configuration spaces available. The `feature_tags` of the info files will contain the names of the configuration options that are activated

A configuration patch is of the form `$AlgoTy_$StorageTy.patch` where `$AlgoTy` and `$StorageTy` are shorthands of the activated configuration option for that category.

## Regression Patches

For each configuration option one or multiple regression patches of 5 severities (`1ms`, `10ms`, `100ms`, `1000ms` and `10000ms`) are available.
The `tags` in the `.info` file will contain the name of the confugration option that is affected. Artificial regressions will be introduced into a specific function in the source code.
Both the regressed function and the severity are indicated in the file name.

TODO: Overview of affected feature regions per regression (?)