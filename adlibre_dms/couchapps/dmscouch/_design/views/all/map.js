function(doc) {
    if (doc.doc_type == "CouchDocument") {
        if (doc.deleted == "deleted") {
            pass
        } else {
            emit(doc._id, {rev: doc._rev});
        }
    }
}