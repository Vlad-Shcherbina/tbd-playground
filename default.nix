let
  pkgs = import <nixpkgs> {};
  hypothesisLatest = pkgs.python34Packages.buildPythonPackage rec {
    name = "hypothesis-1.10.1";
    doCheck = false;
    src = pkgs.fetchurl {
      url = "https://pypi.python.org/packages/source/h/hypothesis/hypothesis-1.10.1.tar.gz";
      md5 = "e8086239a853e1e873cc8074dfccfa74";
    };
    meta = with pkgs.stdenv.lib; {
      description = "A Python library for property based testing";
      homepage = https://github.com/DRMacIver/hypothesis;
      license = licenses.mpl20;
    };
  };

in

{ stdenv          ? pkgs.stdenv
, python          ? pkgs.python3
, nose            ? pkgs.python34Packages.nose
, nosexcover      ? pkgs.python34Packages.nosexcover
, coverage        ? pkgs.python34Packages.coverage
, hypothesis      ? hypothesisLatest
}:
stdenv.mkDerivation {
  name = "tbd-playground-phony";
  version = "0.1.0.0";
  src = ./.;
  buildInputs = [ python
                  nose
                  nosexcover
                  coverage
                  hypothesis ];
}
