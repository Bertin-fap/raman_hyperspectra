__all__ = ["renishaw_1d_si", "witek_2d_si"]


def renishaw_1d_si():

    """
    Get the Renishaw  hyperspectra 'RENISHAW_1D_Si.txt' store in /data
    use in demos

    Arguments:
    
    Returns:
      da (xarray): full spectrum
      da_interp (xarray): full spectrum interpollated on a regular grid
      da_sliced (xarray): sliced spectrum between ldb_dep and lbd_end
      da_sliced_interp (xarray): sliced spectrum between ldb_dep and lbd_end interpollated on a constant grid
    """

    import os
    from ..raman_hyperspectra_read_files import read_RAMAN_RENISHAW_txt_0D

    fname = os.path.join(os.path.dirname(__file__), "RENISHAW_1D_Si.txt")
    da_sliced, da_sliced_interp, da, da_interp = read_RAMAN_RENISHAW_txt_0D(fname)

    return da_sliced, da_sliced_interp, da, da_interp


def witek_2d_si():

    """
    Get the Renishaw 'Large_Area_Scan_000_Spec_As_cut.csv' hyperspectra from github uder the url= URL
    Used for demos
    Arguments:
    
    Returns:
      da (xarray): full spectrum
      da_interp (xarray): full spectrum interpollated on a regular grid
      da_sliced (xarray): sliced spectrum between ldb_dep and lbd_end
      da_sliced_interp (xarray): sliced spectrum between ldb_dep and lbd_end interpollated on a constant grid

    """

    # Standard Libray dependencies
    import os
    import requests
    import tempfile
    import zipfile
    
    # Internal dependencies
    from ..raman_hyperspectra_read_files import read_RAMAN_WITEC_2D

    tmp = tempfile.mkdtemp()  # make a temporary temp directory
    os.chdir(tmp)

    URL = "https://github.com/Bertin-fap/raman-hyperspectra-examples/raw/master/test_files/Large_Area_Scan_000_Spec_As_cut.zip"
    r = requests.get(URL)
    with open(r"data.zip", "wb") as f:  # download the zip file from github
        f.write(r.content)
    with zipfile.ZipFile("data.zip", "r") as my_zip:
        my_zip.extract("Large_Area_Scan_000_Spec_As_cut.csv")

    fname = os.path.join(tmp, "Large_Area_Scan_000_Spec_As_cut.csv")
    da_sliced, da_sliced_interp, da, da_interp = read_RAMAN_WITEC_2D(fname)

    # os.rmdir(tmp) doesn't work the dir is still active to be fixed latter

    return da_sliced, da_sliced_interp, da, da_interp
