{

	"downloads" : [

		"https://github.com/github/cmark/archive/0.28.3.gfm.12.tar.gz",

	],

	"license" : "COPYING",

	"commands" : [

		"mkdir build",
		"cd build && cmake -D CMAKE_INSTALL_PREFIX={buildDir} ..",
		"cd build && make -j {jobs} && make install",

	],

}
