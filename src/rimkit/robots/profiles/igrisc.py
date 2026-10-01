"""IGRIS-C tuning from the approved Kimodo/GEM-X v3 notebooks."""

from dataclasses import replace

from rimkit.robots.joi.body import get_body_joi_mapping
from rimkit.robots.profiles.g1 import G1_DMR_PROFILE

IGRISC_JOI_BODY_NAMES = get_body_joi_mapping("igrisc")

IGRISC_DMR_PROFILE = replace(
    G1_DMR_PROFILE,
    robot_id="igrisc",
    qpos_dim=38,
    joi_bodies=IGRISC_JOI_BODY_NAMES,
    joi_anchor_reference_keys={},
    link_length_base_reference="body_origin",
    trajectory_base_reference="body_origin",
    left_foot_geometry_body_name="Link_Ankle_Roll_Left",
    right_foot_geometry_body_name="Link_Ankle_Roll_Right",
    waist_joint_tokens=("waist_roll", "waist_pitch"),
    pelvis_primary_orientation_weight=0.03,
    pelvis_primary_dynamic_orientation_weight=None,
    pelvis_orientation_axis_length=0.15,
    pelvis_stabilization_strength=0.0,
    pelvis_stabilization_orientation_weight=0.0,
    pelvis_stabilization_linear_speed_low=0.08,
    pelvis_stabilization_linear_speed_high=0.25,
    trunk_position_mode="source_world",
    trunk_position_strength=0.0,
    torso_orientation_joi_key="torso",
    ankle_orientation_axis_length=0.10,
    left_ankle_orientation_joi_key="la_rot",
    right_ankle_orientation_joi_key="ra_rot",
    dmr_temporal_nullspace_gain=0.0,
    pelvis_stabilization_joint_median_window=1,
    pelvis_stabilization_joint_smooth_time=0.0,
    pelvis_stabilization_joint_smooth_max_delta=0.0,
)

__all__ = ["IGRISC_DMR_PROFILE", "IGRISC_JOI_BODY_NAMES"]
