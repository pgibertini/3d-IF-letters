"""
Script extracting the coordinates from the image
Used engauge-digitizer to extract the pixels coordinates
"""
import volmdlr
from volmdlr import Point2D, Vector3D
from volmdlr.core import VolumeModel
from volmdlr.wires import ClosedPolygon2D
from volmdlr.primitives3d import ExtrudedProfile

raw_I = [(0.773757, 0.609392), (0.774033, 1.609945), (0.975691, 1.610221), (0.975414, 0.609669)]

raw_F = [
    (1.074033, 0.409669),
    (1.074033, 1.410221),
    (1.673757, 1.409945),
    (1.674309, 1.251657),
    (1.274586, 1.251657),
    (1.274586, 1.009669),
    (1.624033, 1.009669),
    (1.624309, 0.851657),
    (1.274309, 0.851934),
    (1.274586, 0.409392),
]

coord_I = [(round(x - raw_I[0][0], 2), round(y - raw_I[0][1], 2)) for (x, y) in raw_I]
coord_F = [(round(x - raw_F[0][0], 2), round(y - raw_F[0][1], 2)) for (x, y) in raw_F]

coord_FF = [
    [(0.0, 0.0), (0.0, 0.44), (0.2, 0.44), (0.2, 0.0)],
    [(0.0, 0.44), (0.0, 0.6), (0.55, 0.6), (0.55, 0.44)],
    [(0.0, 0.6), (0.0, 0.84), (0.2, 0.84), (0.2, 0.6)],
    [(0.0, 0.84), (0.0, 1.0), (0.6, 1.0), (0.6, 0.84)],
]

points_I = [Point2D(x, y) for (x, y) in coord_I]
points_F = [Point2D(x, y) for (x, y) in coord_F]
points_FF = [[Point2D(x, y) for (x, y) in coord] for coord in coord_FF]

contour_I = ClosedPolygon2D(points_I)
contour_F = ClosedPolygon2D(points_F)
contours_FF = [ClosedPolygon2D(points) for points in points_FF]

# contour_I.plot()
# contour_F.plot()

volume_I = ExtrudedProfile(
    volmdlr.O3D, volmdlr.X3D, volmdlr.Z3D, contour_I, [], volmdlr.Y3D * points_I[0].point_distance(points_I[-1])
)

volume_F = ExtrudedProfile(
    volmdlr.O3D, volmdlr.X3D, volmdlr.Z3D, contour_F, [], volmdlr.Y3D * points_F[0].point_distance(points_F[-1])
)

volume_FF = VolumeModel(
    [
        ExtrudedProfile(
            volmdlr.O3D,
            volmdlr.X3D,
            volmdlr.Z3D,
            contour,
            [],
            volmdlr.Y3D * contour.points[0].point_distance(contour.points[-1]),
        )
        for contour in contours_FF
    ]
)

# volume_I.babylonjs()
# volume_F.babylonjs()
# volume_FF.babylonjs()

structure = VolumeModel([volume_I, *volume_FF.translation(Vector3D(0.4, 0.4, 0.0)).primitives])
structure.babylonjs()
