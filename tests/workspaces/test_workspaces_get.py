from seamapi import Seam


def test_workspaces_get(seam: Seam):
    ws = seam.workspaces.get()
    assert ws.is_sandbox == True
