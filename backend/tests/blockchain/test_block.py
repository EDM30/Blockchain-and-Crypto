from backend.blockchain.block import block

def test_mine_block():
    last_block = block.genesis()
    data = 'test-data'
    mined_block = block.mine_block(last_block, data)

    assert isinstance(mined_block, block)
    assert mined_block.data == data
    assert mined_block.last_hash == last_block.hash