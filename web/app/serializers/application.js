import Ember from 'ember';
import DRFSerializer from './drf';

export default DRFSerializer.extend({
  extractMeta: function(store, type, payload) {
    let meta = this._super(store, type, payload);
    if (!Ember.isNone(meta)) {
      let totalPages = 1;
      if (!Ember.isNone(meta.next)) {
        let dataKey = Object.keys(payload).find(function(key) { return key !== 'meta'; });
        totalPages = Math.ceil(meta.count / payload[dataKey].length);
      } else if (Ember.isNone(meta.next) && !Ember.isNone(meta.previous)) {
        totalPages = meta.previous + 1;
      }
      meta['total_pages'] = totalPages;
    }
    return meta;
  },
});
