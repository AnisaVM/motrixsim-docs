# 💾 Data (SceneData)

In the previous chapter, we learned that [`SceneModel`](scene_model.md) is used to describe the static physical model. This chapter focuses on the creation and usage of `SceneData`.

## Basic Concepts

`SceneData` is the **dynamic data container** in the MotrixSim simulation system, storing all variables that change during runtime. These data include not only joint positions and velocities, but also the spatial positions and orientations of objects, sensor values, and more.

State updates in `SceneData` require calling kinematic functions to update the system state.

## Creating Data

### Basic Creation

```{literalinclude} ../../../../examples/empty.py
:language: python
:dedent:
:start-after: "# tag::create_data[]"
:end-before:  "# end::create_data[]"
```

For the complete example, see [`examples/empty.py`](../../../../examples/empty.py).

### Multiple Data Instances

MotrixSim supports creating multiple independent `SceneData` instances from the same `SceneModel`, which is useful for parallel experiments, state backups, parameter comparisons, and more.

```{literalinclude} ../../../../examples/model.py
:language: python
:dedent:
:start-after: "# tag::create_data[]"
:end-before:  "# end::create_data[]"
```

Each data instance is independent and can be updated separately.

For the complete example, see [`examples/model.py`](../../../../examples/model.py).

## State Access

### Direct Array Access

`SceneData` provides direct access to system state arrays:

```python
pos = data.dof_pos_array
vel = data.dof_vel_array
```

For detailed `SceneData` attributes, see: [**API Quick Reference - SceneData**](../../api_reference/api_quick_reference.md#-scenedata---状态数据)

### Access via Components

Combined with the Named Access of `SceneModel`, you can access or set specific states through component objects:

```{literalinclude} ../../../../examples/body.py
:language: python
:dedent:
:start-after: "# tag::access_body[]"
:end-before:  "# end::access_body[]"
```

For the complete example, see [`examples/body.py`](../../../../examples/body.py).

## API Reference

For more APIs related to SceneData, see [`SceneData API`]

[`SceneData API`]: motrixsim.SceneData
