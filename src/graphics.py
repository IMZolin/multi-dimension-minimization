import numpy as np
import matplotlib.pyplot as plot

def draw_contoures(self):
    fig, axis = plot.subplots()
    x = np.ndarray((1,len(self.X_step_points_array)))
    y = np.ndarray((1,len(self.X_step_points_array)))
    for i in range(len(self.X_step_points_array)):
        x[0, i] = self.X_step_points_array[i][0]
        y[0, i] = self.X_step_points_array[i][1]
    x_mesh_min = np.min(x)
    x_mesh_max = np.max(x)
    x_mesh_delta = (x_mesh_max - x_mesh_min) / 10
    x_mesh_min -= x_mesh_delta
    x_mesh_max += x_mesh_delta
    y_mesh_min = np.min(y)
    y_mesh_max = np.max(y)
    y_mesh_delta = (y_mesh_max - y_mesh_min) / 10
    y_mesh_min -= y_mesh_delta
    y_mesh_max += y_mesh_delta
    mesh_dest = max(x_mesh_max - x_mesh_min, y_mesh_max - y_mesh_min)
    x_mesh_max = x_mesh_min + mesh_dest
    y_mesh_max = y_mesh_min + mesh_dest
    x_mesh, y_mesh = np.mgrid[x_mesh_min:x_mesh_max:100j, y_mesh_min:y_mesh_max:100j]
    z = np.ndarray(x_mesh.shape)
    for i in range(x_mesh.shape[0]):
        for j in range(x_mesh.shape[1]):
            z[i,j] = self.target_function((x_mesh[i,j], y_mesh[i,j]))
    cs = axis.contour(x_mesh, y_mesh, z, levels=15)
    axis.plot(x.tolist()[0], y.tolist()[0],  'bX--')
    axis.clabel(cs, colors="black")
    fig.set_figwidth(8)
    fig.set_figheight(8)
    plot.ylabel("y")
    plot.xlabel("x")
    plot.title("Линии уровня функции" + self.target_function_str)
    plot.show()