# Patches for HyTeg

This folder contains configuration and regression patches for the `HyTeg` project.

## General

The HyTeg project exposes 2 configuration options that can be switched:

- Solver
  - CGSolver
  - MinResSolver
  - GMRESSolver
- Smoother
  - SORSmoother
  - SymmetricSORSmoother

## Configuration Patches

There are configuration patches for the whole configuration space available. The `feature_tags` of the info files will contain the names of the configuration options that are activated.

A configuration patch is of the form `$PTy_$SolverTy_$SmootherTy.patch` where `$SolverTy` and `$SmootherTy` are shorthands of the activated configuration option for that category.
`$PType` is one of `["p1","p2"]`. It switches the poisson problem to use a different problem setup, so this is loosely comparable to running a different workload [citation needed].

## Regression Patches

For each configuration option one or multiple regression patches of 5 severities (`1ms`, `10ms`, `100ms`, `1000ms` and `10000ms`) are available.
The `tags` in the `.info` file will contain the name of the confugration option that is affected. Artificial regressions will be introduced into a specific function in the source code.

The regressed function will always be the `solve` function of the solver or smoother selected.
