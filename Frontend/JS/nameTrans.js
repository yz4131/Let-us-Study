function short2full(name) {
    var maphash = new Map();

    maphash.set('bl', 'Butler Library');
    maphash.set('aanfal', 'Avery Architectural & Fine Arts Library');
    maphash.set('bcl', 'Barnard College Library');
    maphash.set('bnel', 'Business & Economics Library in Uris');
    maphash.set('eal', 'East Asian Library');
    maphash.set('hsl', 'Health Sciences Library');
    maphash.set('jl', 'Journalism Library');
    maphash.set('ll', 'Law Library');
    maphash.set('sipa', 'Lehman Social Sciences Library');
    maphash.set('ml', 'Mathematics Library');
    maphash.set('mal', 'Music & Arts Library');
    maphash.set('sel', 'Science & Engineering Library');
    maphash.set('tc', 'Teachers College');

    if (maphash.has(name)) {
        return maphash.get(name);
    }
    else {
        console.log("KEY NOT FOUND");
        return name;
    }
}

function full2short(name) {
    var maphash = new Map();

    maphash.set('Butler Library', 'bl');
    maphash.set('Avery Architectural & Fine Arts Library', 'aanfal');
    maphash.set('Barnard College Library', 'bcl');
    maphash.set('Business & Economics Library in Uris', 'bnel');
    maphash.set('East Asian Library', 'eal');
    maphash.set('Health Sciences Library', 'hsl');
    maphash.set('Journalism Library', 'jl');
    maphash.set('Law Library', 'll');
    maphash.set('Lehman Social Sciences Library', 'sipa');
    maphash.set('Mathematics Library', 'ml');
    maphash.set('Music & Arts Library', 'mal');
    maphash.set('Science & Engineering Library', 'sel');
    maphash.set('Teachers College', 'tc');

    if (maphash.has(name)) {
        return maphash.get(name);
    }
    else {
        console.log("KEY NOT FOUND");
        return name;
    }
}