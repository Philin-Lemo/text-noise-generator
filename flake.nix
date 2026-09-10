{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        packages = rec {
          text-noise-generator = pkgs.stdenv.mkDerivation rec {
            pname = "text-noise-generator";
            version = "0.0.5";

            src = ./.;

            nativeBuildInputs = [ pkgs.makeWrapper ];
            buildInputs = [ pkgs.python3 ];

            installPhase = ''
              mkdir -p $out/bin
              cp text_noise_generator.py $out/bin/tng
              chmod +x $out/bin/tng

              # Оборачиваем скрипт, чтобы он всегда вызывал интерпретатор Python из Nix-стора
              wrapProgram $out/bin/tng \
                --prefix PATH : ${pkgs.lib.makeBinPath [ pkgs.python3 ]}
            '';

            meta = with pkgs.lib; {
              description = "Generates text with words from random characters for terminal antistress";
              homepage = "https://github.com/Philin-Lemo/text-noise-generator";
              license = licenses.gpl3Plus; #
              maintainers = [ ];
              mainProgram = "tng";
            };
          };
          default = text-noise-generator;
        };

        devShells.default = pkgs.mkShell {
          buildInputs = [ pkgs.python3 pkgs.git ];
        };
      });
}

