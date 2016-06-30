import numpy as np
import ccdproc
from ccdproc import CCDData
import os
from astropy.io import fits
from astropy import units as u
def combine_files(filelist, outputfile, directory = None):
    # take a list of input files
    if os.path.exists(filelist):
        # load the files
        infiles = np.loadtxt(filelist,dtype=str)
        inputccd = []
        for i in xrange(len(infiles)):
            if directory is not None:
                filename = os.path.join(directory,infiles[i])
            else:
                filename = infiles[i]

            hdu = fits.open(filename,ignore_missing_end=True)
            ccd = CCDData(np.copy(hdu[0].data),unit=u.adu)
            inputccd.append(ccd)
        combo = ccdproc.Combiner(inputccd)
        output = combo.average_combine()
        fits.writeto(outputfile,output.data)
            
            
