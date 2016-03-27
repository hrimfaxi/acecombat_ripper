#!/usr/bin/python2

import os, struct, sys, argparse, subprocess, glob

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--npsf-dir", dest='npsf_dir', help="npsf directory extracted by extract_radio.py",
                    type=str, default="rip")
    parser.add_argument("-x", "--vgstream-binary", dest='vgstream', help="vgstream test decoder binary path", default="vgstream")
    opt = parser.parse_args()

    vgstream_path = os.path.join(opt.vgstream, "test.exe")
    for npsf in glob.glob(os.path.join(opt.npsf_dir, "*.npsf")):
        print ("Processing: %s" % (npsf))
        outfile = os.path.splitext(npsf)[0] + ".wav"
        subprocess.call([vgstream_path, "-o", outfile, npsf])

if __name__ == "__main__":
    main()

# vim: set sw=4 tabstop=4 expandtab:
