<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PrimeStream - Platform Streaming Premium</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #0f172a;
            color: #e2e8f0;
        }
        
        .hero-video {
            background: linear-gradient(to top, #0f172a 10%, transparent 100%);
        }
        
        .movie-card:hover {
            transform: scale(1.05);
            transition: transform 0.3s ease;
            z-index: 10;
        }
        
        .menu-item:after {
            content: '';
            display: block;
            width: 0;
            height: 2px;
            background: #60a5fa;
            transition: width .3s;
        }
        
        .menu-item:hover:after {
            width: 100%;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            height: 6px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1e293b;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #60a5fa;
            border-radius: 4px;
        }
    </style>
</head>
<body class="min-h-screen">
    <!-- Navbar -->
    <nav class="bg-gray-900/80 backdrop-blur-md fixed w-full z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <h1 class="text-xl font-bold text-blue-400">Prime<span class="text-white">Stream</span></h1>
                    </div>
                    <!-- Menu Items -->
                    <div class="hidden md:block">
                        <div class="ml-10 flex items-baseline space-x-6">
                            <a href="#" class="text-white px-3 py-2 rounded-md text-sm font-medium menu-item">Beranda</a>
                            <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium menu-item">Film</a>
                            <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium menu-item">TV Shows</a>
                            <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium menu-item">Kategori</a>
                            <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium menu-item">Daftar Saya</a>
                        </div>
                    </div>
                </div>
                
                <!-- Search and Profile -->
                <div class="hidden md:block">
                    <div class="flex items-center space-x-4">
                        <div class="relative">
                            <input type="text" placeholder="Cari film atau serial..." class="bg-gray-700 text-white px-4 py-1 rounded-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 w-64">
                            <button class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                </svg>
                            </button>
                        </div>
                        <div class="relative group">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/cc305144-0030-4da9-9256-1b95adc5d56a.png" alt="Avatar pengguna dengan latar belakang biru" class="w-8 h-8 rounded-full cursor-pointer">
                            <div class="absolute right-0 mt-2 w-48 bg-gray-800 rounded-md shadow-lg py-1 z-50 hidden group-hover:block">
                                <a href="#" class="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700">Profil</a>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700">Pengaturan</a>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700">Keluar</a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Mobile menu button -->
                <div class="md:hidden flex items-center">
                    <button type="button" id="mobile-menu-button" class="text-gray-300 hover:text-white focus:outline-none">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Mobile menu -->
        <div class="md:hidden hidden" id="mobile-menu">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <a href="#" class="text-white block px-3 py-2 rounded-md text-base font-medium">Beranda</a>
                <a href="#" class="text-gray-300 hover:text-white block px-3 py-2 rounded-md text-base font-medium">Film</a>
                <a href="#" class="text-gray-300 hover:text-white block px-3 py-2 rounded-md text-base font-medium">TV Shows</a>
                <a href="#" class="text-gray-300 hover:text-white block px-3 py-2 rounded-md text-base font-medium">Kategori</a>
                <a href="#" class="text-gray-300 hover:text-white block px-3 py-2 rounded-md text-base font-medium">Daftar Saya</a>
            </div>
        </div>
    </nav>
    
    <!-- Hero Section -->
    <section class="relative h-screen flex items-center hero-video">
        <!-- Background Video Placeholder -->
        <div class="absolute inset-0 overflow-hidden">
            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/b10a7163-c9ed-44ea-a8b4-1f3641a76e35.png" alt="Adegan aksi spektakuler dari film blockbuster superhero" class="w-full h-full object-cover">
        </div>
        
        <div class="absolute inset-0 bg-gradient-to-b from-transparent to-gray-900"></div>
        
        <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-16">
            <div class="max-w-lg md:max-w-2xl">
                <h1 class="text-4xl md:text-6xl font-bold text-white mb-4">Guardians of the Galaxy Vol. 3</h1>
                <div class="flex items-center space-x-4 mb-6">
                    <span class="text-green-500 font-medium">96% Match</span>
                    <span>2023</span>
                    <span class="border border-gray-400 px-1 text-xs">16+</span>
                    <span>2h 30m</span>
                </div>
                <p class="text-gray-300 mb-8">Tim Penjaga Galaksi harus melindungi salah satu dari mereka sendiri. Jika mereka gagal, ini bisa berarti berakhirnya para Penjaga seperti yang kita kenal.</p>
                <div class="flex space-x-4">
                    <button class="bg-white text-gray-900 px-6 py-2 rounded-md font-medium flex items-center hover:bg-opacity-90 transition">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                        </svg>
                        Putar
                    </button>
                    <button class="bg-gray-600 bg-opacity-70 text-white px-6 py-2 rounded-md font-medium flex items-center hover:bg-opacity-50 transition">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        Info Lainnya
                    </button>
                </div>
            </div>
        </div>
    </section>
    
    <main class="relative z-10 -mt-20">
        <!-- Trending Now -->
        <section class="mb-12 px-4 sm:px-6 lg:px-8">
            <div class="max-w-7xl mx-auto">
                <h2 class="text-xl font-bold mb-4">Trending Sekarang</h2>
                <div class="relative">
                    <div class="flex space-x-4 overflow-x-auto pb-6 scrollbar-hide -mx-4 px-4">
                        <!-- Movie Cards -->
                        <div class="movie-card flex-shrink-0 w-48 sm:w-56 relative group">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/80e8225c-2b40-4b4b-9c3b-657dcce339ac.png" alt="Poster film John Wick dengan adegan aksi high-octane" class="w-full h-64 sm:h-72 object-cover rounded-lg">
                            <div class="absolute inset-0 bg-gray-900 bg-opacity-0 group-hover:bg-opacity-70 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 rounded-lg">
                                <button class="bg-white text-gray-900 p-2 rounded-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                            <div class="mt-2">
                                <h3 class="font-medium">John Wick 4</h3>
                                <div class="flex items-center text-sm text-gray-400">
                                    <span>2023</span>
                                    <span class="mx-2">•</span>
                                    <span>Film</span>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Repeat similar cards -->
                        <div class="movie-card flex-shrink-0 w-48 sm:w-56 relative group">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/c07bfd38-ba4f-463a-b987-e525d3646c82.png" alt="Poster The Last of Us menampilkan karakter utama di dunia pasca-apokaliptik" class="w-full h-64 sm:h-72 object-cover rounded-lg">
                            <div class="absolute inset-0 bg-gray-900 bg-opacity-0 group-hover:bg-opacity-70 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 rounded-lg">
                                <button class="bg-white text-gray-900 p-2 rounded-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                            <div class="mt-2">
                                <h3 class="font-medium">The Last of Us</h3>
                                <div class="flex items-center text-sm text-gray-400">
                                    <span>2023</span>
                                    <span class="mx-2">•</span>
                                    <span>Serial TV</span>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 3 more cards -->
                        <div class="movie-card flex-shrink-0 w-48 sm:w-56 relative group">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/0e9280c4-dc2c-4bc5-b11a-33073a772cd9.png" alt="Poster Avatar 2 dengan setting bawah air yang memukau" class="w-full h-64 sm:h-72 object-cover rounded-lg">
                            <div class="absolute inset-0 bg-gray-900 bg-opacity-0 group-hover:bg-opacity-70 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 rounded-lg">
                                <button class="bg-white text-gray-900 p-2 rounded-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                            <div class="mt-2">
                                <h3 class="font-medium">Avatar 2</h3>
                                <div class="flex items-center text-sm text-gray-400">
                                    <span>2022</span>
                                    <span class="mx-2">•</span>
                                    <span>Film</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Continue Watching -->
        <section class="mb-12 px-4 sm:px-6 lg:px-8">
            <div class="max-w-7xl mx-auto">
                <h2 class="text-xl font-bold mb-4">Lanjut Menonton</h2>
                <div class="bg-gray-800 rounded-lg p-4">
                    <div class="flex items-center space-x-4">
                        <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/54a399f9-05d3-4a67-8c04-35dc103ed889.png" alt="Thumbnail serial Stranger Things dengan nuansa retro" class="w-20 h-12 sm:w-32 sm:h-20 object-cover rounded">
                        <div class="flex-1">
                            <h3 class="font-medium">Stranger Things</h3>
                            <p class="text-sm text-gray-400 mb-2">Season 4, Episode 5</p>
                            <div class="w-full bg-gray-700 rounded-full h-1.5">
                                <div class="bg-blue-500 h-1.5 rounded-full w-3/4"></div>
                            </div>
                            <div class="flex justify-between text-xs text-gray-400 mt-1">
                                <span>45:32</span>
                                <span>1:02:15</span>
                            </div>
                        </div>
                        <button class="bg-white text-gray-900 p-2 rounded-full">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Categories Section -->
        <section class="mb-16 px-4 sm:px-6 lg:px-8">
            <div class="max-w-7xl mx-auto">
                <h2 class="text-xl font-bold mb-6">Jelajahi Kategori</h2>
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
                    <a href="#" class="category-card bg-gray-800 p-4 rounded-lg text-center hover:bg-gray-700 transition">
                        <div class="bg-blue-500 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z" />
                            </svg>
                        </div>
                        <span>Aksi</span>
                    </a>
                    
                    <a href="#" class="category-card bg-gray-800 p-4 rounded-lg text-center hover:bg-gray-700 transition">
                        <div class="bg-green-500 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                        </div>
                        <span>Animasi</span>
                    </a>
                    
                    <!-- More categories -->
                    <a href="#" class="category-card bg-gray-800 p-4 rounded-lg text-center hover:bg-gray-700 transition">
                        <div class="bg-yellow-500 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                        </div>
                        <span>Komedi</span>
                    </a>
                    
                    <a href="#" class="category-card bg-gray-800 p-4 rounded-lg text-center hover:bg-gray-700 transition">
                        <div class="bg-red-500 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                            </svg>
                        </div>
                        <span>Sci-Fi</span>
                    </a>
                    
                    <a href="#" class="category-card bg-gray-800 p-4 rounded-lg text-center hover:bg-gray-700 transition">
                        <div class="bg-purple-500 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                            </svg>
                        </div>
                        <span>Thriller</span>
                    </a>
                    
                    <a href="#" class="category-card bg-gray-800 p-4 rounded-lg text-center hover:bg-gray-700 transition">
                        <div class="bg-pink-500 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z" />
                            </svg>
                        </div>
                        <span>Dokumenter</span>
                    </a>
                </div>
            </div>
        </section>
        
        <!-- Popular Shows -->
        <section class="mb-12 px-4 sm:px-6 lg:px-8">
            <div class="max-w-7xl mx-auto">
                <h2 class="text-xl font-bold mb-4">Serial Populer</h2>
                <div class="relative">
                    <div class="flex space-x-4 overflow-x-auto pb-6 scrollbar-hide -mx-4 px-4">
                        <!-- Series Cards -->
                        <div class="movie-card flex-shrink-0 w-48 sm:w-56 relative group">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/00ae0f2d-0c7b-4dfe-9eb9-3906b59813f5.png" alt="Poster serial Game of Thrones dengan setting fantasi epik" class="w-full h-64 sm:h-72 object-cover rounded-lg">
                            <div class="absolute inset-0 bg-gray-900 bg-opacity-0 group-hover:bg-opacity-70 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 rounded-lg">
                                <button class="bg-white text-gray-900 p-2 rounded-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                            <div class="mt-2">
                                <h3 class="font-medium">Game of Thrones</h3>
                                <div class="flex items-center text-sm text-gray-400">
                                    <span>2011-2019</span>
                                    <span class="mx-2">•</span>
                                    <span>8 Musim</span>
                                </div>
                            </div>
                        </div>
                        
                        <!-- More series -->
                        <div class="movie-card flex-shrink-0 w-48 sm:w-56 relative group">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/b86ff3e5-3c9d-44be-b950-f9529d1748cb.png" alt="Poster Stranger Things dengan nuansa retro dan misterius" class="w-full h-64 sm:h-72 object-cover rounded-lg">
                            <div class="absolute inset-0 bg-gray-900 bg-opacity-0 group-hover:bg-opacity-70 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 rounded-lg">
                                <button class="bg-white text-gray-900 p-2 rounded-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                            <div class="mt-2">
                                <h3 class="font-medium">Stranger Things</h3>
                                <div class="flex items-center text-sm text-gray-400">
                                    <span>2016-Sekarang</span>
                                    <span class="mx-2">•</span>
                                    <span>4 Musim</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    
    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 pt-12 pb-6">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mb-8">
                <div>
                    <h3 class="text-white text-sm font-semibold mb-4">Tentang Kami</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-sm hover:text-white">Tentang PrimeStream</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Karir</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Kebijakan Privasi</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Syarat & Ketentuan</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 class="text-white text-sm font-semibold mb-4">Bantuan</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-sm hover:text-white">Pusat Bantuan</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Akun Saya</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Cara Menonton</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Pengaturan Rekomendasi</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 class="text-white text-sm font-semibold mb-4">Kontak</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-sm hover:text-white">Kontak Kami</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Media</a></li>
                        <li><a href="#" class="text-sm hover:text-white">Sponsorship</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3 class="text-white text-sm font-semibold mb-4">Download Aplikasi</h3>
                    <div class="flex space-x-4 mb-4">
                        <a href="#">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/5f65eb3c-5202-4d44-9bd1-48e44eea56f3.png" alt="Download di App Store" class="h-10">
                        </a>
                        <a href="#">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/8bc939e5-2632-4084-8e2b-eb9dab24c9d7.png" alt="Download di Google Play" class="h-10">
                        </a>
                    </div>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M22.675 0h-21.35c-.732 0-1.325.593-1.325 1.325v21.351c0 .731.593 1.324 1.325 1.324h11.495v-9.294h-3.128v-3.622h3.128v-2.671c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12v9.293h6.116c.73 0 1.323-.593 1.323-1.325v-21.35c0-.732-.593-1.325-1.325-1.325z" />
                            </svg>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-

