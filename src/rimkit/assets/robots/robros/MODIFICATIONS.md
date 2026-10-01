# IGRIS-C integration

The packaged serial 31-DOF research model is the validated model used by
`28_kimodo_to_igrisc_explained_v3.ipynb` and
`116_gemx_to_igrisc_explained_v3.ipynb`. It is retained as a snapshot rather
than regenerated from the newer upstream v2 xacro at package build time.

- `igrisc/igris_c.xml` retains the torso-root tree and original joint order.
- `igrisc/igris_c_retarget.xml` reverses the waist chain and places the free
  joint on `Link_Waist_Pitch`, preserving scalar joint meanings.
- The fixed `Link_Waist_Pitch_aux` is the neutral hip midpoint, independent
  of hip articulation; its neutral x coordinate aligns with `base_link`.
- Hip, knee, elbow, wrist, and hand aux bodies are position landmarks.
- Physical ankle-roll bodies are rotation targets; sole/toe landmarks are
  contact references. Ground-distance queries use physical foot geometry.
- Hand rotation retains the frame-zero realized-pose calibration.
- Output articulated columns retain the original XML joint order.

Only meshes referenced by the retained MJCF are packaged. The scene lives
under `assets/scenes/igrisc.xml` and adds the RIMKit shared floor.

The retained upstream `package.xml` declares `BSD 3-clause`. The inspected
upstream revision has no standalone license file; the license declaration
is retained verbatim rather than assigning a fabricated copyright notice.
