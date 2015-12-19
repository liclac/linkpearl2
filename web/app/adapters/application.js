import DRFAdapter from './drf';

export default DRFAdapter.extend({
  addTrailingSlashes: false,
  shouldReloadAll(store, snapshotRecordArray) {
    return snapshotRecordArray.length == 0;
  },
  shouldReloadRecord(store, snapshot) {
    return false;
  },
  shouldBackgroundReloadRecord(store, snapshot) {
    return true;
  },
  shouldBackgroundReloadAll(store, snapshotRecordArray) {
    return true;
  }
});
