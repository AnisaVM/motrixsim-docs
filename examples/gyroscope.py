# Copyright (C) 2020-2025 Motphys Technology Co., Ltd. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import time

import numpy as np

from motrixsim import SceneData, load_model, step
from motrixsim.render import RenderApp

# Mouse controls:
# - Press and hold left button then drag to rotate the camera/view
# - Press and hold right button then drag to pan/translate the view


# This is an interesting gyroscopic demo.
def main():
    # Create render window for visualization
    render = RenderApp()
    # The scene description file
    path = "examples/assets/gyroscope.xml"
    # Load the scene model
    model = load_model(path)
    # Create the render instance of the model
    render.launch(model)
    # Create the physics data of the model
    data = SceneData(model)

    body_fb = model.get_body(model.get_body_index("gyro")).floatingbase
    body_fb.set_local_angular_velocity(data, np.array([0, 0, 50]))

    while True:
        t = time.monotonic()
        # Step the physics world
        step(model, data)
        # Sync render objects from physic world
        render.sync(data)

        passed = time.monotonic() - t

        if passed < model.options.timestep:
            # Sleep to maintain the desired timestep
            time.sleep(model.options.timestep - passed)


if __name__ == "__main__":
    main()
