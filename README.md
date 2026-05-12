# Multi-Agent CFD System

A production-style multi-agent CFD orchestration framework for combustion chamber optimization.

## Features

- Multi-agent architecture
- Long-horizon optimization workflow
- Autonomous simulation iteration
- CFD tool orchestration
- HPC scheduling abstraction
- Failure reflection & recovery
- Trajectory memory
- Optimization loop

## Architecture

Planner Agent
↓
Simulation Agent
↓
Tool Calling Layer
↓
Analysis Agent
↓
Critic Agent
↓
Optimization Agent

## Run

```bash
pip install -r requirements.txt
python main.py
```
